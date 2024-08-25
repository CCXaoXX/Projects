import jieba
import wordcloud
import pandas as pd

ans = ''
txt = pd.read_csv('E:/片片.csv', header=None, error_bad_lines=False)[0]
for i in txt:
    ans += i
    ans += ' '

words = jieba.lcut(ans)  # 精确分词
newtxt = ''.join(words)  # 空格拼接
wordcloud = wordcloud.WordCloud(font_path='simhei.ttf').generate(newtxt)
wordcloud.to_file('中文词云图.jpg')
