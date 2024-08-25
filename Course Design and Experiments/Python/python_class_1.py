from decimal import *
import math
from fractions import Fraction
from time import *
import numpy as np

'''
#  1.1
x = float(input('输入：'))
print('该数的平方根为：', math.sqrt(x))

result_1 = math.sqrt(x + 1) - math.sqrt(x)
print('普通计算方法1：', result_1)

result_2 = 1 / (math.sqrt(x + 1) + math.sqrt(x))
print('普通计算方法2：', result_2)

# 1.2
x = 0.0

for i in range(1000000):
    x = x + 0.1
print("sum result = ", x)

# 1.3
x = 1e10
y = 1e-8
for i in range(10000000):
    x = x + y
print(x)

x = 1e10
y = 1e-8
temp = 0
for i in range(10000000):
    temp += y
x += temp
print(x)

# 1.4
x = Decimal("0.0")
for i in range(1000000):
    x = x + Decimal("0.1")
print("sum result = ", x)

# 1.5
print(Fraction(5, 10), Fraction(3, 15))
print(Fraction(1, 3) + Fraction(1, 7))
print(Fraction(5, 3) * Fraction(6, 7) * Fraction(3, 2))
'''

# 2
time0 = time()
x = 2
f = 1
countMul = 0
countAdd = 0
for i in range(100000):
    f = f + (i+2) * pow(x, (i + 1))
    countMul += 1
    countAdd += 1
print("结果为：", len(str(f)))
time1 = time()
print("time = %.2g s\n" % (time1 - time0))
print("乘法次数为：", countMul)
print("加法次数为：", countAdd)


time0 = time()
x = 2
powN = 100000
AN = powN + 1
countMul_1 = 0
countAdd_1 = 0
S = AN
for i in range(powN, 0, -1):
    S = S * x + i
    countMul_1 += 1
    countAdd_1 += 1
print("结果为：", len(str(S)))
time1 = time()
print("time = %.2g s\n" % (time1 - time0))
print("乘法次数为：", countMul_1)
print("加法次数为：", countAdd_1)


# 3
a = 2
limit = 1e-20


def f(x):
    return x * x - a


x_low = float(input('X下限：'))
x_high = float(input('X上限：'))

count = 0
while(x_high - x_low) * (x_high - x_low) > limit:
    x_mid = (x_high + x_low) / 2
    count += 1
    if f(x_mid) > 0:
        x_high = x_mid
    else:
        x_low = x_mid

    print("\n{:} {:} {:}".format(count, x_low, x_high))
    print('大小：', (x_high + x_low) / 2)
    print('正负:', f((x_high + x_low) / 2))