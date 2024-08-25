import numpy as np


def search_init(n, c, w, v):  # 初始化价值表
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]  # 置零，表示初始状态
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            value[i][j] = value[i - 1][j]
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:  # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
    return value


def re_back(n, c, w, value):  # 回溯寻找最大价值子集
    x = [False for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    max_v = []
    for i in range(n):
        if x[i]:
            max_v.append(i + 1)
    print('\n最大价值子集为:\n', max_v)
    print('最大价值为:', value[n][c])
    return max_v


if __name__ == '__main__':
    try:
        n = int(input('请输入物品个数(n>=0)：\n'))
        W = int(input('请输入书包容量(W>=0)：\n'))
        w = np.random.randint(low=1, high=W, size=n, dtype=np.int64)
        print('\n随机生成的物品质量为：\n', w)
        v = np.random.randint(low=1, high=W, size=n, dtype=np.int64)
        print('随机生成的物品价值为：\n', v)
        value = search_init(n, W, w, v)
        max_v = re_back(n, W, w, value)
        max_w = sum(w[i-1] for i in max_v)
        print('最大质量为：', max_w)
        input('\n输入回车离开')
    except:
        print('\n输入错误')
