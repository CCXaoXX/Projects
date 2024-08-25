import jieba

# 语料库
waste = []
standard_waste = []
file_waste = r'waste.txt'  # 相对路径
with open(file_waste, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()
    for line in lines:
        change_line = line.strip()
        waste.append(change_line)

for i in range(0, len(waste)):
    for word in waste[i].split():
        standard_waste.append(word)


# 关键字提取
def token(sentence):
    after_word = []
    word = jieba.lcut(sentence, cut_all=True)
    for w in word:
        if w in standard_waste:
            after_word.append(w)
    final_word = ' '.join(after_word)
    return final_word


# 输入
sen = input()


# 输出
out = token(sen)
print(out)

