# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 20:31:34 2022

@author: Wu Xinghua
"""

from matplotlib import pyplot as plt
import numpy as np


def fixpt(f, x, epsilon=1.0E-5, N=500, store=False):
    y = f(x)
    n = 0
    if store:
        Values = [(x, y)]
    while abs(y - x) >= epsilon and n < N:
        x = f(x)
        n += 1
        y = f(x)
        if store:
            Values.append((x, y))
    if store:
        return y, Values
    else:
        if n >= N:
            return "No fixed point for given start value"
        else:
            return x, n, y


# define f
def f(x):
    return ((-58 * x - 3) / (7 * x ** 3 - 13 * x ** 2 - 21 * x - 12)) ** (1 / 2)


# find fixed point
res, points = fixpt(f, 1.5, store=True)

# create mesh for plots
xx = np.arange(1.2, 1.6, 1e-5)

plt.plot(xx, f(xx), 'b')
plt.plot(xx, xx, 'r')


# plot lines
count = 1
for x, y in points:
    plt.xlim((min(points[0]) - 0.1, x + 0.1))  # range
    plt.title((count, round((x + y) / 2, 3)))  # tittle
    count += 1  # 计数

    plt.plot([x, x], [x, y], 'g')
    plt.pause(0.1)
    plt.plot([x, y], [y, y], 'g')
    plt.pause(0.1)


# show result
plt.show()