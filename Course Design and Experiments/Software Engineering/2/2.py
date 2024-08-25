import numpy as np


def date(k):
    n = pow(2, k)  # 选手
    board = np.zeros((n, n))
    for i in range(2):  # 初始化左上角棋盘
        for j in range(2):
            if i == j:
                board[i][j] = 1
            else:
                board[i][j] = 2
    for i in range(1, k):
        add = pow(2, i)
        for i in range(add):  # 左下角的子表中项为左上角子表对应项加2^i
            for j in range(add):
                board[i + add][j] = board[i][j] + add
        for i in range(add):  # 右上角的子表等于左下角子表
            for j in range(add):
                board[i][j + add] = board[i + add][j]
        for i in range(add):  # 右下角的子表等于左上角的子表
            for j in range(add):
                board[i + add][j + add] = board[i][j]
    np.array(board)
    return np.delete(board, 0, axis=1)


if __name__ == '__main__':
    try:
        k = int(input('请输入k(共有n=2^k个选手)：\n'))
        print('日程表为（大小{}）：\n{}'.format(date(k).shape, date(k)))
        input('输入回车离开')
    except:
        print('输入错误')