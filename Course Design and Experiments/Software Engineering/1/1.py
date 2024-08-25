import numpy as np
import matplotlib.pyplot as plt


class Board:
    def __init__(self, size, x, y):
        self.special_block = (x, y)
        self.board = np.zeros((size, size), dtype=int)  # 棋盘大小 2^k * 2^k
        self.board[x][y] = (size * size - 1) / 3 + 1  # 特殊方格
        # self.board[x][y] = -1
        self.t = 1
        self.size = size

    def visualize(self):
        plt.imshow(self.board, cmap=plt.cm.Purples)  # 颜色
        plt.colorbar()
        plt.title('chessboard')
        plt.savefig('chessboard.jpg')
        plt.show()

    def fill_block(self, x, y):
        if self.board[x][y] == 0:
            self.board[x][y] = self.t
        else:
            raise Exception  # 异常处理

    def fill(self, s_x, s_y, size, c_x, c_y):
        if size == 1:
            return
        pos = (round((c_x - s_x + 1) / size), round((c_y - s_y + 1) / size))
        center = (round(s_x + size / 2 - 1), round(s_y + size / 2 - 1))
        ls = [(0, 0), (0, 1), (1, 0), (1, 1)]  # 代表四个子区块
        for i in ls:
            if i != pos:  # 如果不是原有特殊点所在区块，则构造特殊点并填充
                x = center[0] + i[0]
                y = center[1] + i[1]
                self.fill_block(x, y)
        self.t += 1  # 标记号加一，标记下一骨牌
        for i in ls:
            if i != pos:  # 如果不是原有特殊点所在区块，则构造特殊点位置(x, y)
                x = center[0] + i[0]
                y = center[1] + i[1]
                x1 = s_x + i[0] * (size / 2)
                y1 = s_y + i[1] * (size / 2)
                self.fill(x1, y1, size / 2, x, y)
            else:  # 如果是原有特殊点所在区块
                x1 = s_x + i[0] * (size / 2)
                y1 = s_y + i[1] * (size / 2)
                self.fill(x1, y1, size / 2, c_x, c_y)


if __name__ == '__main__':
    try:
        k = eval(input("请输入K(棋盘大小为2^K * 2^K，K>=0):\n"))
        loc_x = eval(input("请输入特殊方格横坐标(X>=0):\n"))
        loc_y = eval(input("请输入特殊方格纵坐标(Y>=0):\n"))
        size = pow(2, k)
        b = Board(size, loc_x, loc_y)
        b.fill(0, 0, size, loc_x, loc_y)
        b.visualize()
        print('棋盘如下：\n', b.board)
        input("输入回车离开")
    except:
        print('输入错误')