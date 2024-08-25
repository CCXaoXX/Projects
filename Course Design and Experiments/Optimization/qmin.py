import numpy as np
import matplotlib.pyplot as plt


def complicated_func(x):
    '''
        目标函数
    :param x:
    :return:
    '''
    return x * x * x - 2 * x + 1


def parabolic_search(f, a, b, epsilon=0.01):  # 精度
    '''
        抛物线法，迭代函数
    :param f: 目标函数
    :param a:   起始点
    :param b:   终止点
    :param epsilon: 阈值
    :return:
    '''
    h = (b - a) / 2
    s0 = a
    s1 = a + h
    s2 = b
    f0 = f(s0)
    f1 = f(s1)
    f2 = f(s2)
    h_mean = (4 * f1 - 3 * f0 - f2) / (2 * (2 * f1 - f0 - f2)) * h
    s_mean = s0 + h_mean
    f_mean = f(s_mean)
    # 调试
    k = 0
    while s2 - s0 > epsilon:
        h = (s2 - s0) / 2
        h_mean = (4 * f1 - 3 * f0 - f2) / (2 * (2 * f1 - f0 - f2)) * h
        s_mean = s0 + h_mean
        f_mean = f(s_mean)
        if f1 <= f_mean:
            if s1 < s_mean:
                s2 = s_mean
                f2 = f_mean
                # 重新计算一次，书上并没有写，所以导致一直循环
                s1 = (s2 + s0)/2
                f1 = f(s1)
            else:
                s0 = s_mean
                f0 = f_mean
                s1 = (s2 + s0)/2
                f1 = f(s1)
        else:
            if s1 > s_mean:
                s2 = s1
                s1 = s_mean
                f2 = f1
                f1 = f_mean
            else:
                s0 = s1
                s1 = s_mean
                f0 = f1
                f1 = f_mean
        print([k, (s2 - s0), f_mean, s_mean])
        k += 1
    return s_mean, f_mean


if __name__ == '__main__':
    x = np.linspace(0, 3, 200)  # 起始区间
    y = []
    index = 0
    for i in x:
        y.append(complicated_func(x[index]))
        index += 1
    plt.plot(x, y)
    plt.show()

    result = parabolic_search(complicated_func, 0, 3)  # 起始区间
    print(result)

    # x = np.linspace(0, 2, 200)
    # plt.plot(x, phi(x))
    # plt.show()
    # result = parabolic_search(phi, 0, 2.0)
    # print(result)
