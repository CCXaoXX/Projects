import numpy as np


def Jacobi(A, b, x0, xstar):
    k = 0
    while True:
        for i in range(0, n):
            sum = 0.0
            for j in range(0, i):
                sum = sum + A[i][j] * x0[j]
            for j in range(i + 1, n):
                sum = sum + A[i][j] * x0[j]
            xstar[i] = (b[i] - sum) / A[i][i]
        temp = np.fabs(xstar[0] - x0[0])
        for j in range(1, n):
            if np.fabs(xstar[j] - x0[j]) > temp:
                temp = np.fabs(xstar[j] - x0[j])
        for j in range(0, n):
            x0[j] = xstar[j]
        k = k + 1
        if temp < 1.0e-6 or k > 1000:
            break
    print("Jacobi迭代次数:", k)


def Gauss(A, b, x0, xstar):
    k = 0
    while True:
        for i in range(0, n):
            sum = 0.0
            for j in range(0, i):
                sum = sum + A[i][j] * xstar[j]
            for j in range(i + 1, n):
                sum = sum + A[i][j] * x0[j]
            xstar[i] = (b[i] - sum) / A[i][i]
        temp = np.fabs(xstar[0] - x0[0])
        for j in range(1, n):
            if np.fabs(xstar[j] - x0[j]) > temp:
                temp = np.fabs(xstar[j] - x0[j])
        for j in range(0, n):
            x0[j] = xstar[j]
        k = k + 1
        if temp < 1.0e-6 or k > 1000:
            break
    print("Gauss迭代次数:", k)


def swap(a, b, k, n):
    ans = 0
    for i in range(k, n):
        if ans < np.fabs(a[i][k]):
            ans = a[i][k]
            maxn = i
    a[[k, maxn], :] = a[[maxn, k], :]
    b[k], b[maxn] = b[maxn], b[k]


def gauss2(a, b):
    m, n = a.shape
    l = np.zeros((n, n))
    for i in range(n):
        if a[i][i] == 0:
            print("no answer")

    for k in range(n - 1):
        swap(a, b, k, n)
        for i in range(k + 1, n):
            l[i][k] = a[i][k] / a[k][k]
            for j in range(m):
                a[i][j] = a[i][j] - l[i][k] * a[k][j]
            b[i] = b[i] - l[i][k] * b[k]

    x = np.zeros(n)
    x[n - 1] = b[n - 1] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            b[i] -= a[i][j] * x[j]
        # 自增自减
        x[i] = b[i] / a[i][i]
    for i in range(n):
        print("x" + str(i + 1) + " =", x[i])


# 数据操作
n = 5
A = 1. / (np.arange(1, n + 1) + np.arange(0, n)[:, np.newaxis])
b = np.zeros(n, float)
x0 = np.zeros(n, float)
Jex = np.zeros(n, float)
GSex = np.zeros(n, float)
for i in range(0, n):
    b[i] = round(sum(A[i]), 3)
    x0[i] = 1

Jacobi(A, b, x0, Jex)
Gauss(A, b, x0, GSex)
print("Jacobi迭代结果:", Jex)
print("Gauss迭代结果:", GSex)

gauss2(A, b)