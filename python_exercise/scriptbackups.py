import json
import os
import pandas as pd
import re
from collections import Counter


# 拼写检查
def words(text): return re.findall(r'\w+', text.lower())


WORDS = Counter(words(open('D:\cc\\big.txt').read()))


def P(word, N=sum(WORDS.values())):
    return WORDS[word] / N


def correction(word):
    return max(candidates(word), key=P)


def candidates(word):
    return known([word]) or known(edits1(word)) or known(edits2(word)) or [word]


def known(words):
    return set(w for w in words if w in WORDS)


def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in WORDS)


def known(words):
    return set(w for w in words if w in WORDS)


def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=WORDS.get)


# 过滤表情
def filter_emoji(content):
    try:
        cont = re.compile(u'['u'\U0001F300-\U0001F64F' u'\U0001F680-\U0001F6FF'u'\u2600-\u2B55]+')
    except re.error:
        cont = re.compile(u'('u'\ud83c[\udf00-\udfff]|'u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'u'[\u2600-\u2B55])+')
        return cont.sub(u'', content)


# re过滤
def re_clean(text):
    text = re.sub(r"(回复)?(//)?\s*@\S*?\s*(:| |$)", " ", text)  # 去除@
    text = re.sub(r"\[\S+\]", "", text)  # 去除表情符号
    URL_REGEX = re.compile(
        r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))',
        re.IGNORECASE)
    text = re.sub(URL_REGEX, "", text)  # 去除网址
    text = re.sub('[^a-zA-Z0-9]', ' ', text).lower()  # 保留英文内容以及数字
    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"\s+", " ", text)  # 去除多余空格
    text = text.split()
    return text


# 使用停用词表
stop = []
standard_stop = []
file_stop = r'D:\\cc\\stopwords.txt'
with open(file_stop, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()
    for line in lines:
        change_line = line.strip()
        stop.append(change_line)

for i in range(0, len(stop)):
    for word in stop[i].split():
        standard_stop.append(word)

# 批量处理文件
folder_name = 'D:\Dataset\labeled\-positive\data\-tweet\\'
test_id = 1
file_names = os.listdir(folder_name)
os.chdir(folder_name)
num = 0

# 文件数
file_num = len([lists for lists in os.listdir(folder_name) if os.path.isfile(os.path.join(folder_name, lists))])
print('共有文件{:}个'.format(file_num))

# json内容提取
for i in range(round(file_num * 0.2), file_num):
    after_out = []
    path = 'D:\Dataset\labeled\-positive\data\-tweet\\' + file_names[i]
    data = open(path, 'r')
    for eachLine in data:
        # 得到text内容
        line = eachLine.strip()
        line = line.strip(',')
        js = json.loads(line)
        # 停用词表 正则表达式处理
        change_out = js['text'].replace('\n', '').replace(',', ' ')
        change_out = re_clean(change_out)
        for wi in change_out:
            if wi not in standard_stop:  # 停用词表
                # wi = correct(wi)  # 拼写检查
                after_out.append(wi)
        # 转为字符串
        out = list(map(str, after_out))
        out = ' '.join(out)
        ensure_ascii = False
        out = pd.DataFrame([out])
    if not str(out[0][0]) == '':
        out[1] = '1'
        out.to_csv('D:\cc\shujv2\\trainData.csv', mode='a', header=False, index=False)
        print('存入第{}个json成功'.format(i + 1))
        num += 1

print('\n共存进文件{}个'.format(num))
