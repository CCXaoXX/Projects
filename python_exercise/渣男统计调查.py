#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

fig = plt.figure(figsize=(20, 10), dpi=80)

x1 = range(11, 31)
##20年
y1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]

x2 = range(11, 31)
y2 = [2, 3, 5, 3, 5, 7, 8, 0, 4, 7, 8, 6, 1, 2, 3, 4, 4, 2, 3, 5]
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

plt.scatter(x1, y1, color="black", label="劲铧")
plt.scatter(x2, y2, color="blue", label="陈宸")

plt.plot(x1, y1, color='r', label="劲铧", linestyle='--', linewidth=4, alpha=0.5)
plt.plot(x2, y2, color='orange', label="陈宸", linestyle='--', linewidth=4, alpha=0.5)

for x, y in zip(x1, y1):
    plt.text(x, y + 0.1, '%.0f' % y, ha='center', va='bottom', fontsize=10.5)
for x, y in zip(x2, y2):
    plt.text(x, y + 0.1, '%.0f' % y, ha='center', va='bottom', fontsize=10.5)

plt.xticks(x1[::1], fontproperties=font, size=14)
plt.yticks(y2[::1], fontproperties=font, size=14)

plt.xlabel("年龄", FontProperties=font, size=20)
plt.ylabel("个数", FontProperties=font, size=20)

plt.title("渣男每年渣女统计", FontProperties=font, size=30, c="pink")

plt.legend(prop=font, loc="best")
plt.text(11, 8, "扫黄人出品", FontProperties=font, size=19)

plt.show()
