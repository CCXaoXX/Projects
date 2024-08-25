import numpy as np
from scipy import integrate


# 3
def fun1(x):  # 待求解数值积分x^2
    return pow(x, 2)


def TX(f, a, b):  # 梯形公式 f为待求解积分 a为积分下限 b为积分上限
    TX = 0.5 * (b - a) * (f(a) + f(b))
    print("梯形公式计算结果为：", TX)
    return TX


a, b = 0, 1
pred = TX(fun1, a, b)  # 公式结果
real = integrate.quad(fun1, 0, 1)[0]  # 真实结果
loss = pow((real - pred), 2)  # 误差
print('真实数据为：', round(real, 3))
print('误差为：', round(loss, 3))


# 4
def fun2(x):  # 待求解数值积分x^0.5
    return pow(x, 0.5)


def XPS(f, a, b):
    XPS = (b - a) * (f(a) + 4 * f((a + b) / 2) + f(b)) / 6.0
    print("辛普森公式计算结果为：", round(XPS, 3))
    return XPS


a, b = 1, 2
pred = XPS(fun2, a, b)  # 公式结果
real = integrate.quad(fun2, 1, 2)[0]  # 真实结果
loss = pow((real - pred), 2)  # 误差
print('真实数据为：', round(real, 3))
print('误差为：', round(loss, 3))


# 6
def fun3(x):
    return 7 * pow(x, 6) - 4 * pow(x, 3) + 1


def cotes4(f, a, b):
    h = (b - a) / 4
    x0, x1, x2, x3, x4 = a, a + h, a + 2 * h, a + 3 * h, a + 4 * h
    cotes_4 = (b - a) * (7 * f(x0) + 32 * f(x1) + 12 * f(x2) + 32 * f(x3) + 7 * f(x4)) / 90
    print("四阶牛顿－柯特斯公式计算结果为：", round(cotes_4, 3))
    return cotes_4


def cotes6(f, a, b):
    h = (b - a) / 6
    x0, x1, x2, x3, x4, x5, x6 = a, a + h, a + 2 * h, a + 3 * h, a + 4 * h, a + 5 * h, a + 6 * h
    cotes_6 = (b - a) * (41 * f(x0) + 216 * f(x1) + 27 * f(x2) + 272 * f(x3) + 27 * f(x4) + 216 * f(x5) + 41 * f(x6)) / 840
    print("六阶牛顿－柯特斯公式计算结果为：", round(cotes_6, 3))
    return cotes_6


a, b = 1, 2
pred = cotes4(fun3, a, b)  # 四阶公式结果
real = integrate.quad(fun3, 1, 2)[0]  # 四阶真实结果
loss = pow((real - pred), 2)  # 四阶误差
print('真实数据为：', round(real, 3))
print('误差为：', round(loss, 3))

pred = cotes6(fun3, a, b)  # 六阶公式结果
loss = pow((real - pred), 2)  # 六阶误差
print('真实数据为：', round(real, 3))
print('误差为：', round(loss, 3))


# 16
x0 = 1.0
x1 = 1.1
x2 = 1.2

y0 = 0.25
y1 = 0.2268
y2 = 0.2066

h = 0.1

f0 = (-3 * y0 + 4 * y1 - y2) / (2 * h)
f1 = (-y0 + y2) / (2 * h)
f2 = (y0 - 4 * y1 + 3 * y2) / (2 * h)

f = (y0 - 2 * y1 + y2) / pow(h, 2)

print("x0的一阶导数为：", round(f0, 3))
print("x0的二阶导数为：", round(f, 3))
print("x1的一阶导数为：", round(f1, 3))
print("x1的二阶导数为：", round(f, 3))
print("x2的一阶导数为：", round(f2, 3))
print("x2的二阶导数为：", round(f, 3))