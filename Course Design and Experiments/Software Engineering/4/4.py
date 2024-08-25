def test_search(k):  # 主函数
    global n, x, X, t, best_t, best_x
    if k == n:
        j2_t = []
        s = 0
        for i in range(n):
            s += t[x[i]][0]
            j2_t.append(s + t[x[i]][1])
        total_t = sum(j2_t)
        if best_t == 0 or total_t < best_t:
            best_t = total_t
            best_x = x[:]
    else:
        for i in range(n):
            x[k] = i
            if not cutting(k, x, t, best_t):
                test_search(k + 1)


def cutting(k, x, t, best_t):  # 剪枝函数
    if x[:k + 1].count(x[k]) > 1:
        return True
    j2_t = []
    s = 0
    for i in range(k + 1):
        s += t[x[i]][0]
        j2_t.append(s + t[x[i]][1])
    total_t = sum(j2_t)
    if total_t > best_t > 0:
        return True
    return False


if __name__ == '__main__':
    try:
        n = int(input('请输入作业数(n>=0)\n'))
        t = [[0 for col in range(2)] for row in range(n)]
        for i in range(n):
            print("请输入作业{}在机器M1，M2所需的时间".format(i + 1))
            for j in range(2):
                t[i][j] = int(input("M" + str(j + 1) + "[" + str(i + 1) + "]="))
        x = [0] * n
        X = []
        best_x = []
        best_t = 0
        test_search(0)
        for i in range(len(best_x)):
            best_x[i] += 1
        print('\n耗时最短的作业顺序为：\n', best_x)
        print('共耗时：', best_t)
        input('\n输入回车离开')
    except:
        print('输入错误')
