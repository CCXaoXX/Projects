import math


def function(x):  # 待求函数
    return 3 * x ** 2 - 2 * math.tan(x)


def six18(f, a, b, k):
    e = 1e-4  # 精度
    r = 0.618
    b1 = a + r * (b - a)
    a1 = b - r * (b - a)
    k += 1
    if b - a < e:
        return (a + b) / 2
    elif f(a1) < f(b1):
        print(k, (a + b1) / 2)
        return six18(function, a, b1, k)
    elif f(a1) > f(b1):
        print(k, (a1 + b) / 2)
        return six18(function, a1, b, k)
    else:
        return (a1 + b1) / 2  # 最低点在两值中间


six18(function, 0, 1, 0)
