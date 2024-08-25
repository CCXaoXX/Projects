import numpy as np


# 2.1
def gauss1(data):
    j = 0
    line_size = len(data)
    while j < line_size - 1:
        line = data[j]
        temp = line[j]
        templete = []
        for x in line:
            x = x / temp
            templete.append(x)
        data[j] = templete
        flag = j + 1
        while flag < line_size:
            templete1 = []
            temp1 = data[flag][j]
            i = 0
            for x1 in data[flag]:
                if x1 != 0:
                    x1 = x1 - (temp1 * templete[i])
                    templete1.append(x1)
                else:
                    templete1.append(0)
                i += 1
            data[flag] = templete1
            flag += 1
        j += 1

    parameters = []
    i = line_size - 1
    rol_size = len(data[0])
    flag_rol = rol_size - 2
    while i >= 0:
        operate_line = data[i]
        if i == line_size - 1:
            parameter = operate_line[rol_size - 1] / operate_line[flag_rol]
            parameters.append(parameter)
        else:
            flag_j = (rol_size - flag_rol - 2)
            temp2 = operate_line[rol_size - 1]
            result_flag = 0
            while flag_j > 0:
                temp2 -= operate_line[flag_rol + flag_j] * parameters[result_flag]
                result_flag += 1
                flag_j -= 1
            parameter = temp2 / operate_line[flag_rol]
            parameters.append(parameter)
        flag_rol -= 1
        i -= 1
    return parameters


mat = [[2.51, 1.48, 4.53, 0.05], [1.48, 0.93, -1.3, 1.03], [2.68, 3.04, -1.48, -0.53]]
results = gauss1(mat)
print("x1 = " + str(results[2]) + "\n" + "x2 = " + str(results[1]) + "\n" + "x3 = " + str(results[0]))


# 2.2
def swap(a, b, k, n):
    ans = 0
    for i in range(k, n):
        if ans < np.fabs(a[i][k]):
            ans = a[i][k]
            maxn = i
    a[[k, maxn], :] = a[[maxn, k], :]
    b[k], b[maxn] = b[maxn], b[k]


# 主算法
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
        x[i] = b[i] / a[i][i]
    for i in range(n):
        print("x" + str(i + 1) + " =", x[i])


x = np.array([[2.51, 1.48, 4.53], [1.48, 0.93, -1.3], [2.68, 3.04, -1.48]])
y = np.array([0.05, 1.03, -0.53])
gauss2(x, y)


# 3.1
def gauss3(a, b):
    m, n = a.shape
    l = np.zeros((n, n))
    for i in range(n):
        if a[i][i] == 0:
            print("no answer")

    for k in range(n - 1):
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
        x[i] = b[i] / a[i][i]

    for i in range(n):
        print("x" + str(i + 1) + " = ", x[i])
    print("x" " = ", x)


A = np.array([[1, 2, 1, -2], [2, 5, 3, -2], [-2, -2, 3, 5], [1, 3, 2, 3]])
b = np.array([4, 7, -1, 0])
gauss3(A, b)


# 3.2
def LU(A):
    n = len(A[0])
    L = np.zeros([n, n])
    U = np.zeros([n, n])
    for i in range(n):
        L[i][i] = 1
        if i == 0:
            U[0][0] = A[0][0]
            for j in range(1, n):
                U[0][j] = A[0][j]
                L[j][0] = A[j][0] / U[0][0]
        else:
            for j in range(i, n):
                temp = 0
                for k in range(0, i):
                    temp = temp + L[i][k] * U[k][j]
                U[i][j] = A[i][j] - temp
            for j in range(i + 1, n):
                temp = 0
                for k in range(0, i):
                    temp = temp + L[j][k] * U[k][i]
                L[j][i] = (A[j][i] - temp) / U[i][i]
    return L, U


def get_x(A, b):
    L, U = LU(A)
    n = len(A)
    y = np.zeros((n, 1))
    b = np.array(b).reshape(n, 1)
    for i in range(len(A)):
        t = 0
        for j in range(i):
            t += L[i][j] * y[j][0]
        y[i][0] = b[i][0] - t

    X = np.zeros((n, 1))
    for i in range(len(A) - 1, -1, -1):
        t = 0
        for j in range(i + 1, len(A)):
            t += U[i][j] * X[j][0]
        t = y[i][0] - t
        if t != 0 and U[i][i] == 0:
            return 0
        X[i] = t / U[i][i]

    return X


A = np.array([[1, 2, 1, -2], [2, 5, 3, -2], [-2, -2, 3, 5], [1, 3, 2, 3]])
b = np.array([4, 7, -1, 0])
x = get_x(A, b)
print(x)

# 7
x = np.matrix([[-2, 1, 0, 0], [1, -2, 1, 0], [0, 1, -2, 1], [0, 0, 1, -2]])

x_norm_1 = np.linalg.norm(x, ord=1)
x_norm_2 = np.linalg.norm(x, ord=2)
x_norm_n = np.linalg.norm(x, ord=np.inf)
x_cond = np.linalg.cond(x, p=2)

print(x)
print(x_norm_1)
print(x_norm_2)
print(x_norm_n)
print(x_cond)

# 8
A = np.array([[10, 7, 8, 7], [7, 5, 6, 5], [8, 6, 10, 9], [7, 5, 9, 10]])
b = np.array([32, 23, 33, 31])
b_ = np.array([32.1, 22.9, 33.1, 30.9])
x = get_x(A, b)
x_ = get_x(A, b_)
print(x)
print(x_)

x_norm_1 = np.linalg.norm(x, ord=1)
xx_norm_1 = np.linalg.norm(x_, ord=1)
inf1 = (xx_norm_1 - x_norm_1) / x_norm_1

x_norm_n = np.linalg.norm(x, ord=np.inf)
xx_norm_n = np.linalg.norm(x_, ord=np.inf)
inf2 = (xx_norm_n - x_norm_n) / x_norm_n

print("x1:", round(inf1, 3))
print("xn:", round(inf2, 3))

b_norm_1 = np.linalg.norm(b, ord=1)
bb_norm_1 = np.linalg.norm(b_, ord=1)
inf3 = (bb_norm_1 - b_norm_1) / b_norm_1

b_norm_n = np.linalg.norm(b, ord=np.inf)
bb_norm_n = np.linalg.norm(b_, ord=np.inf)
inf4 = (bb_norm_n - b_norm_n) / b_norm_n

print("b1:", round(inf3, 3))
print("bn:", round(inf4, 3))


# 9
def Astringency_Jacobi(A):
    length, width = np.shape(A)
    D = np.mat(np.diag(np.diag(A)))
    L = -1 * np.triu(A, 1)
    U = -1 * np.tril(A, -1)
    H = np.eye(length) - D.I * A
    eig, _ = np.linalg.eig(H)
    spectral_radius = max(abs(eig))
    if spectral_radius < 1:
        print('此方程组收敛,谱半径为', round(spectral_radius, 5))
    else:
        print('Jacobi迭代法不收敛,谱半径为', round(spectral_radius, 5))


A = np.array([[1, 2, -2], [1, 1, 1], [2, 2, 1]])
B = np.array([[2, -1, 1], [1, 1, 1], [1, 1, -2]])
Astringency_Jacobi(A)
Astringency_Jacobi(B)


def Astringency(mx):
    L, D, U = [], [], []
    for i in range(len(mx)):
        L.append([]), D.append([]), U.append([])
        for j in range(len(mx)):
            if i > j:
                L[i].append(mx[i][j]), D[i].append(0), U[i].append(0)
            if i == j:
                L[i].append(0), D[i].append(mx[i][j]), U[i].append(0)
            if i < j:
                L[i].append(0), D[i].append(0), U[i].append(mx[i][j])

    ld = L
    for i in range(len(mx)):
        for k in range(len(mx)):
            ld[i][k] = L[i][k] + D[i][k]

    G = np.dot(-np.linalg.inv(ld), U)
    e, v = np.linalg.eig(G)
    for i in range(len(e)):
        count = 0
        if abs(e[i]) < 1:
            continue
        else:
            count = count + 1
            print(abs(e[i]))

    if count == 0:
        return True
    else:
        print("迭代法不收敛")
        return False


A = np.array([[1, 2, -2], [1, 1, 1], [2, 2, 1]])
B = np.array([[2, -1, 1], [1, 1, 1], [1, 1, -2]])
print(Astringency(A))
print(Astringency(B))


# 10
def jacobi(a, b, c=0.0001, d=30):
    x1 = np.zeros(a.shape[1])
    x2 = np.zeros(a.shape[1])
    k = 0
    while k < d:
        k = k + 1
        print('k=', k)
        for i in range(a.shape[1]):
            x2[i] = (-a[i].dot(x1) + b[i] + a[i, i] * x1[i]) / a[i, i]
        if np.max(np.abs(x2 - x1)) <= c:
            print("x%d=" % k, x2)
            print(np.max(np.abs(x2 - x1)))
            break
        print("x%d=" % k, x2)
        x1 = x2.copy()
    return x2


a = np.array([[11, -3, -2], [-1, 5, -3], [-2, -12, 19]])
b = np.array([[3], [6], [-7]])
jacobi(a, b)


def Gauss_seidel(mx, mr, n=100, e=0.0001):
    if len(mx) == len(mr):
        if Astringency(mx) == 1:
            x = []
            for i in range(len(mr)):
                x.append([0])
            count = 0
            while count < n:
                tempx = np.copy(x)
                for i in range(len(x)):
                    ri = mr[i][0]
                    for k in range(len(mx[i])):
                        if k != i:
                            ri = ri - mx[i][k] * x[k][0]
                    ri = ri / mx[i][i]
                    x[i][0] = ri
                print("第{}次迭代的值为：{}".format(count + 1, x))
                ee = []
                for i in range(len(x)):
                    ee.append(abs(x[i][0] - tempx[i][0]))
                em = max(ee)
                print("第{}、{}次迭代间误差值为:{}".format(count, count + 1, em))
                if em < e:
                    return x
                count += 1
            return False
        else:
            print("使用迭代法不收敛")
    else:
        print("此方程无解")


a = np.array([[11, -3, -2], [-1, 5, -3], [-2, -12, 19]])
b = np.array([[3], [6], [-7]])
Gauss_seidel(a, b)