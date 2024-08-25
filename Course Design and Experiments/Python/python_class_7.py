from math import e
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import metrics
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']


# 2
def Euler():
    print('{:>3s}{:>8s}{:>9s}{:>12s}{:>9s}{:>9s}'.format('x', 'y_e', 'y_i', 'y_pro', 'y_rk', 'y_c'))
    for i in range(num):
        # 显示Euler
        y_e.append(round(y_e[i] + h * fun(x[i], y_e[i]), 3))

        # 隐式Euler
        y_i1 = y_i[i] + h * fun(x[i], y_i[i])
        y_i2 = y_i[i] + h * fun(x[i + 1], y_i1)
        while abs(y_i2 - y_i1) > 1e-6:
            y_i1 = y_i2
            y_i2 = y_i[i] + h * fun(x[i + 1], y_i1)
        y_i.append(y_i2)

        # 改进Euler
        y_p.append(y_pro[i] + h * fun(x[i], y_pro[i]))
        y_pro.append(round(y_pro[i] + h / 2 * (fun(x[i], y_pro[i]) + fun(x[i + 1], y_p[i])), 3))

        # 龙格-库塔
        k1 = fun(x[i], y_rk[i])
        k2 = fun(x[i] + h / 2, y_rk[i] + h / 2 * k1)
        k3 = fun(x[i] + h / 2, y_rk[i] + h / 2 * k2)
        k4 = fun(x[i] + h, y_rk[i] + h * k3)
        y_rk.append(round(y_rk[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4), 3))

        # 解析解
        y_c.append(round((-2 + x[i] + 3 * e ** (-0.5 * 0)), 3))

        print('{}{:>10f}{:>10f}{:>10f}{:>10f}{:>10f}\n'.format(
            round(x[i + 1], 1),
            y_e[i + 1],
            y_i[i + 1],
            y_pro[i + 1],
            y_rk[i + 1],
            y_c[i + 1]))

    plt.plot(x, y_e, label='显式Euler', color='r', marker='+')
    plt.plot(x, y_i, label='隐式Euler', color='c', marker='>')
    plt.plot(x, y_pro, label='改进Euler', color='b', marker='3')
    plt.plot(x, y_rk, label='龙格-库塔', color='m', marker='d')
    plt.plot(x, y_c, label='解析解', color='g', marker='o')
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('函数图像')
    plt.show()


def fun(x0, y0):
    return x0 - y0 / 2


# 初始值
y_e = []  # 显式
y_i = []  # 隐式
y_pro = []  # 改进
y_p = []  # 改进
y_rk = []  # 龙格-库塔
y_c = []  # 解析解
x = []
h = 0.5  # 步长
num = 7

x.append(0.0)
y_e.append(1)  # 显式
y_i.append(1)  # 隐式
y_pro.append(1)  # 改进
y_rk.append(1)  # 龙格-库塔
y_c.append(1)  # 解析解
for i in range(num):
    x.append(round(x[0] + i * h, 1))
Euler()

print('显式Euler的误差为：', round(metrics.mean_squared_error(y_e, y_c), 3))
print('隐式Euler的误差为：', round(metrics.mean_squared_error(y_i, y_c), 3))
print('改进Euler的误差为：', round(metrics.mean_squared_error(y_pro, y_c), 3))
print('龙格-库塔的误差为：', round(metrics.mean_squared_error(y_rk, y_c), 3))


# 5
def f(x, y):
    return -y / (x + pow(y, 2))


x0 = 0
y0 = 1
xn = 3
h = 0.5
print('\nx         y ')
while x0 <= xn:
    print('\n{:.3f}  {:.3f} '.format(x0, y0))
    k1 = h * f(x0, y0)
    x1 = x0 + h
    k2 = h * f(x1, y0 + k1)
    y1 = y0 + (k1 + k2) / 2
    x0 = x1
    y0 = y1
