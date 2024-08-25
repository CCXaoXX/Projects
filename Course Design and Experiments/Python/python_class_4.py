import numpy as np
from sympy import *


# 1
def LA(x0, x1, x2, y0, y1, y2, x):
    l0 = ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))
    l1 = ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))
    l2 = ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))
    L2 = y0 * l0 + y1 * l1 + y2 * l2
    return round(L2, 3)


def fun(x):
    return 1 / x


x0 = 2
x1 = 2.5
x2 = 4
y0 = fun(x0)
y1 = fun(x1)
y2 = fun(x2)

x = 3

res = LA(x0, x1, x2, y0, y1, y2, x)
print("结果：", res)
print("误差：", round(fun(3) - res, 3))


# 2
# LA
def L(x, f):
    X = symbols("x")
    m = x.size
    L = 0
    for i in range(m):
        temp = 1
        for j in range(m):
            if i != j:
                temp = temp * ((X - x[j]) / (x[i] - x[j]))
        L = L + temp * f[i]
    return L


x1 = np.array([0, 1, 2])
y1 = np.array([1, 2, 3])
x2 = np.array([1, 3, 4, 7])
y2 = np.array([0, 2, 15, 12])

print('L1:', simplify(L(x1, y1)))
print('L2:', simplify(L(x2, y2)))


# N
def cs(x, f, start, end, res):
    if (end - start) == 1:
        res[end - 1][end - start - 1] = (f[end] - f[start]) / (x[end] - x[start])
        return res[end - 1][end - start - 1]
    res[end - 1][end - start - 1] = (cs(x, f, start + 1, end, res) - cs(x, f, start, end - 1, res)) / (
            x[end] - x[start])
    return res[end - 1][end - start - 1]


def Newton(x, f):
    res = np.ones([x.size - 1, x.size - 1]) * np.inf
    cs(x, f, 0, x.size - 1, res)
    X = symbols("x")
    y = f[0]
    for i in range(x.size - 1):
        temp = 1
        for j in range(i + 1):
            temp = temp * (X - x[j])
        temp = res[i, i] * temp
        y = y + temp
    return y


res1 = np.ones([x1.size - 1, x1.size - 1]) * np.inf
res2 = np.ones([x2.size - 1, x2.size - 1]) * np.inf
cs(x1, y1, 0, x1.size - 1, res1)
cs(x2, y2, 0, x2.size - 1, res2)

print(res1)
print(res2)


Y1 = Newton(x1, y1)
Y2 = Newton(x2, y2)

print("N(x)_1=", simplify(Y1))
print("N(x)_2=", simplify(Y2))

# F
x3 = np.array([1, 3, 4, 7, 4])
y3 = np.array([0, 2, 15, 12, 4])
print('L3:', simplify(L(x3, y3)))

Y3 = Newton(x3, y3)
print("N(x)_3=", simplify(Y3))
