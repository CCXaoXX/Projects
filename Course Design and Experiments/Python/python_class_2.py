import numpy as np
import pandas as pd
import math
from scipy.misc import derivative


# part1
def fun1(x):
    return 7 * pow(x, 5) - 13 * pow(x, 4) - 21 * pow(x, 3) - 12 * pow(x, 2) + 59 * x + 3


def fun2(x):
    return pow((13 * pow(x, 4) + 21 * pow(x, 3) + 12 * pow(x, 2) - 58 * x - 3) / 7, 1 / 5)


def fun3(x):
    return (13 + 21 / x + 12 / pow(x, 2) - 58 / pow(x, 3) - 3 / pow(x, 4)) / 7


def fun4(x):
    return pow((12 * pow(x, 2) - 58 * x - 3) / (7 * pow(x, 2) - 13 * x - 21), 1 / 3)


def fun5(x):
    return pow((-58 * x - 3) / (7 * pow(x, 3) - 13 * pow(x, 2) - 21 * x - 12), 1 / 2)


def Aitken(x0, epsilon, iternum, fun):
    xk_1 = x0
    for i in range(iternum):
        y = fun(xk_1)
        z = fun(y)
        if (z - 2 * y + xk_1) != 0:
            xk = xk_1 - (y - xk_1) ** 2 / (z - 2 * y + xk_1)
            print("第", i + 1, "次迭代 ", "x=", xk)
            if abs(xk - xk_1) < epsilon:
                return xk
            else:
                xk_1 = xk


def Steffensen(x, epsilon, iternum, fun):
    for k in range(iternum):
        a = x
        b = fun(x)
        c = fun(fun(x))
        x = x - ((b - x) ** 2) / (c - 2 * b + a)
        k += 1
        print("第", k, "次迭代 ", "x=", x)
        if abs(x - a) < epsilon:
            return x


# part2
def fun_2(x):
    return 7 * pow(x, 5) - 13 * pow(x, 4) - 21 * pow(x, 3) - 12 * pow(x, 2) + 58 * x + 3


def Newton(x0, epsilon, iternum, fun):
    xk_1 = x0
    for i in range(iternum):
        fx = fun(xk_1)
        fdx = derivative(fun, xk_1, dx=1e-6)
        if fdx != 0:
            xk = xk_1 - fx / fdx
            print("第", i + 1, "次迭代 ", "x=", xk)
            if abs(xk - xk_1) < epsilon:
                return xk
            else:
                xk_1 = xk


def Secant1(func, x0, x1, theta, iternum):
    for i in range(iternum):
        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        print("第", i + 1, "次迭代 ", "x=", x2)
        x1 = x2
        if abs(func(x2)) < theta:
            return x2


def Secant2(func, x0, x1, theta, iternum):
    for i in range(iternum):
        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        print("第", i + 1, "次迭代 ", "x=", x2)
        if abs(func(x2)) < theta:
            return x2
        x0 = x1
        x1 = x2


# Secant1(fun_2, 1, 2, pow(10, -5), 50)
# Secant2(fun_2, 1, 2, pow(10, -5), 50)
# Newton(1.5, pow(10, -5), 50, fun_2)
# Aitken(1.5, pow(10, -5), 5000, fun_2)
# Steffensen(1.5, pow(10, -5), 5000, fun_2)


# part3
def twice(func, x0, x1, theta, iternum):
    for i in range(iternum):
        if (x1 - x0) * (x1 - x0) > theta:
            x = x0 + (x1 - x0) / 2
            if np.sign(func(x)) * np.sign(func(x0)) < 0:
                x1 = x
            else:
                x0 = x
            print("第", i + 1, "次迭代 ", "x=", x)


def normal(x0, epsilon, iternum, fun):
    for i in range(iternum):
        x = x0 - fun(x0) / derivative(fun, x0, dx=1e-6)
        if abs(x - x0) > epsilon:
            x0 = x
            print("第", i + 1, "次迭代 ", "x=", x)
        else:
            break

# normal(1.5, pow(10, -5), 10, fun_2)
# twice(fun_2, 1, 2, pow(10, -5), 100)
