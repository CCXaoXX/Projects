import numpy as np
import pandas as pd
import math
import random


def data_init(block):  # 初始化函数
    for i in range(size):
        a = Block(numpage=-1, accessed=0)
        block.append(a)


def page_find(block, curpage):  # 查找物理块中是否有该页面
    for i in range(size):
        if block[i].numpage == curpage:
            return i
    return -1


def change_find(block):  # 查找置换的页号
    pos = 0
    for i in range(size):
        if block[i].accessed > block[pos].accessed:
            pos = i
    return pos


def display(block):  # 可视化函数
    for i in range(size):
        if block[i].numpage != -1:
            print(block[i].numpage)
    print('\n')


def random_fun(order):  # 生成随机指令序列
    for i in range(320):
        count = random.randint(0, 319)
        order.append(count)


def space_find(block):  # 寻找空闲物理块
    for i in range(size):
        if block[i].numpage == -1:
            return i
    return -1


def FIFO(block, n):
    print('过程如下：')
    for i in range(320):
        count = order[i]
        curpage = math.floor(count / 10)  # 页号向下取整
        exsist = page_find(block, curpage)
        if exsist == -1:
            space = space_find(block)
            if space == -1:
                exchange = change_find(block)
                block[exchange].numpage = curpage
                display(block)
                n = n + 1
                block[exchange].accessed = -1
            else:
                block[space].numpage = curpage
                display(block)
                n = n + 1
        else:
            for i in range(size):
                if block[i].numpage != -1:
                    print(block[i].numpage)
            print("\n已存在，页号为", exsist, '\n')
        for j in range(size):
            block[j].accessed += 1
    print("缺页次数为：", n, '次\n缺页率为：', n / 320.0 * 100, "%")


def LRU(blcok, n):
    print('过程如下：')
    for i in range(320):
        count = order[i]
        curpage = math.floor(count / 10)  # 页号向下取整
        exsist = page_find(block, curpage)
        if exsist == -1:
            space = space_find(block)
            if space == -1:
                exchange = change_find(block)
                block[exchange].numpage = curpage
                display(block)
                n = n + 1
                block[exchange].accessed = -1
            else:
                block[space].numpage = curpage
                display(block)
                n = n + 1
        else:
            block[exsist].accessed = -1
            for i in range(size):
                if block[i].numpage != -1:
                    print(block[i].numpage)
            print("\n已存在，页号为", exsist, '\n')
        for j in range(size):
            block[j].accessed += 1
    print("缺页次数为：", n, '次\n缺页率为：', n / 320.0 * 100, "%")


def OPT(block, n):
    print('过程如下：')
    for i in range(320):
        count = order[i]
        curpage = math.floor(count / 10)  # 页号向下取整
        exsist = page_find(block, curpage)
        if exsist == -1:
            space = space_find(block)
            if space == -1:
                for h in range(size):
                    for k in range(i, 320):
                        if block[h].numpage != order[k] / 10:
                            block[h].accessed = 1000
                        else:
                            block[h].accessed = k
                            break
                exchange = change_find(block)
                block[exchange].numpage = curpage
                display(block)
                n = n + 1
            else:
                block[space].numpage = curpage
                display(block)
                n = n + 1
        else:
            for i in range(size):
                if block[i].numpage != -1:
                    print(block[i].numpage)
            print("\n已存在，页号为", exsist, '\n')
    print("缺页次数为：", n, '次\n缺页率为：', n / 320.0 * 100, "%")


class Block(object):
    def __init__(self, numpage=-1, accessed=0):
        self.numpage = numpage  # 页号
        self.accessed = accessed  # 访问情况，数值表示多久未被访问


if __name__ == '__main__':
    try:
        # 共有4个内存块，一个内存块存放一个页面，一个页面存放10条指令，共32个页面,指令在页面中顺序存放
        size = 4  # 内存块数目
        count = 0  # 记录指令的序号
        n = 0  # 缺页数目
        block = []  # 内存块
        order = []  # 指令
        random_fun(order)
        matrix = pd.DataFrame(np.array([order]).reshape([32, 10]))
        print("随机生成的矩阵如下:\n", matrix)
        data_init(block)
        while True:
            a = input("\n请输入\t1.FIFO\t2.LRU\t3.OPT\n")
            a = int(a)
            if a == 1:
                FIFO(block, n)
                input('\n输入回车离开')
            elif a == 2:
                LRU(block, n)
                input('\n输入回车离开')
            elif a == 3:
                OPT(block, n)
                input('\n输入回车离开')
    except:
        input('输入错误\n输入回车离开')

