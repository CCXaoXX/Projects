import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.optimize import leastsq


mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

x = np.arange(0, 10, 1, dtype='float')
y = np.array([67.025, 68.008, 69.803, 72.024, 73.400, 72.063, 74.669, 74.487, 74.065, 76.777], dtype='float')

# 作图
plt.figure()
plt.title(u'世界石油产量变化')
plt.xlabel(u'年')
plt.ylabel(u'桶/天(*10^5)')
plt.axis([1994, 2004, 60, 80])
plt.grid(True)
plt.plot(x + 1994, y, 'k.')


# 二次
param0 = [0, 0, 0]


def quadratic_fun(s, x):
    k1, k2, b = s
    return k1 * pow(x, 2) + k2 * x + b


# 三次
param1 = [0, 0, 0, 0]


def cubic_fun(s, x):
    k1, k2, k3, b = s
    return k1 * pow(x, 3) + k2 * pow(x, 2) + k3 * x + b


# 四次
param2 = [0, 0, 0, 0, 0]


def fpower_fun(s, x):
    k1, k2, k3, k4, b = s
    return k1 * pow(x, 4) + k2 * pow(x, 3) + k3 * pow(x, 2) + k4 * x + b


# 自定义函数
param3 = [0, 0, 0]


def myfuns(s, x):
    a, b, c = s
    return a * np.exp(-b * (x - c))


# 求出残差
def dist(a, fun, x, y):
    return fun(a, x) - y


funs = [quadratic_fun, cubic_fun, fpower_fun, myfuns]
params = [param0, param1, param2, param3]
colors = ['blue', 'red', 'black', 'green']
fun_name = ['quadratic_fun', 'cubic_fun', '4power_fun', 'a*exp(-b*(t-c)']

for i, (func, param, color, name) in enumerate(zip(funs, params, colors, fun_name)):
    var = leastsq(dist, param, args=(func, x, y))
    plt.plot(x + 1994, func(var[0], x), color)
    print("[%s] 二范数： %.3f, abs(bias): %.3f, bias-std: %.3f" %
          (name, ((y - func(var[0], x)) ** 2).sum(), (y - func(var[0], x)).std(), (abs(y - func(var[0], x))).mean()))

plt.legend(['sample data', '二次曲线', '三次曲线', '四次曲线', '直线'], loc='upper left')
plt.show()


f1 = np.polyfit(x, y, 2)
f2 = np.polyfit(x, y, 3)
f3 = np.polyfit(x, y, 4)
p1 = np.poly1d(f1)
p2 = np.poly1d(f2)
p3 = np.poly1d(f3)
print('p1 is :\n', p1)
print('p2 is :\n', p2)
print('p3 is :\n', p3)

print('直线的预测值：\n', round(myfuns([67.782, -0.013, 0.208], 2010 - 1994), 3))
print('二次多项式的预测值：\n', round(quadratic_fun([p1[2], p1[1], p1[0]], 2010 - 1994), 3))
print('三次多项式的预测值：\n', round(cubic_fun([p2[3], p2[2], p2[1], p2[0]], 2010 - 1994), 3))
print('四次多项式的预测值：\n', round(fpower_fun([p3[4], p3[3], p3[2], p3[1], p3[0]], 2010 - 1994), 3))