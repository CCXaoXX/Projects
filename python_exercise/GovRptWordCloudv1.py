#GovRptWordCloudv1.py
import jieba
import wordcloud
f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud( font_path = "msyh.ttc", width = 1000, height = 700, background_color="white")
w.generate(txt)
w.to_file("grwordcloud.png")
print("运行成功")
