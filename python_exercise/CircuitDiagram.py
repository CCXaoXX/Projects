import random


# 判断函数
def judge15():
    print('此函数为judge15\n')
    X004 = random.choice([0, 1])
    print("此时X004的值为{}\n".format(X004))
    if X004:
        print('电路联通！')
    else:
        print('电路不联通！')


def judge17():
    print('此函数为judge17\n')
    M100 = random.choice([0, 1])
    print("此时M100的值为{}\n".format(M100))
    if M100:
        print('电路联通！')
    else:
        print('电路不联通！')


def judge23():
    print('此函数为judge23\n')
    M103 = random.choice([0, 1])
    print("此时M103的值为{}\n".format(M103))
    if M103:
        print('电路联通！')
    else:
        print('电路不联通！')


def judge25():
    print('此函数为judge25\n')
    M103 = random.choice([0, 1])
    M101 = random.choice([0, 1])
    print("此时M103的值为{}\n此时M101的值为{}\n".format(M103, M101))
    if M103 or M101:
        print('电路联通！')
    else:
        print('电路不联通！')


def judge28():
    print('此函数为judge28\n')
    M102 = random.choice([0, 1])
    print("此时M102的值为{}\n".format(M102))
    if M102:
        print('电路联通！')
    else:
        print('电路不联通！')


def judge19():
    # 随机复制
    print('此函数为judge19\n')
    M200 = random.choice([0, 1])
    M100 = random.choice([0, 1])
    T1 = random.choice([0, 1])
    print('此时M100的值为{}\n此时M200的值为{}\n此时T1的值为{}\n'.format(M100, M200, T1))
    if M100:
        print('电路联通！')
    else:
        if M200 and T1:
            print('电路联通！')
        else:
            print('电路不连通！')


judge19()
judge25()