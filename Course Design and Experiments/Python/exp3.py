import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
import pylab as pl

# range生成x
x1 = np.arange(-5, 5.1, 0.5)  # 21条数据
y1 = np.array(
    [-0.1923, -0.2118, -0.2353, -0.2642, -0.3, -0.3448, -0.4000, -0.4615, -0.5000, -0.4000, 0, 0.4000, 0.5000, 0.4615,
     0.4000, 0.3448, 0.3000, 0.2642, 0.2353, 0.2118, 0.1923])
y2 = np.array(
    [0.0016, 0.002, 0.0025, 0.0033, 0.0044, 0.0064, 0.0099, 0.0175, 0.0385, 0.1379, 1.0000, 0.1379, 0.0385, 0.0175,
     0.0099, 0.0064, 0.0044, 0.0033, 0.0025, 0.0020, 0.0016])

# 转化成list
data1 = np.zeros((21, 2))
data2 = np.zeros((21, 2))
for i in range(len(x1)):
    data1[i][0] = x1[i]
    data1[i][1] = y1[i]
    data2[i][0] = x1[i]
    data2[i][1] = y2[i]


# 自定义函数
def fun1(x):
    return x / (1 + pow(x, 2))


def fun2(x):
    return x / (1 + 25 * pow(x, 2))


# 真实结果
y_1_real = fun1(-3.75)
y_2_real = fun1(0.25)
y_3_real = fun2(-3.75)
y_4_real = fun2(0.25)

print('y1(-3.75) = ', round(y_1_real, 3))
print('y1(0.25) = ', round(y_2_real, 3))
print('y2(-3.75) = ', round(y_3_real, 3))
print('y2(0.25) = ', round(y_4_real, 3))


# 1
def Lg(data, testdata):
    predict = 0
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]
    if testdata in data_x:
        return data_y[data_x.index(testdata)]
    else:
        for i in range(len(data_x)):
            af = 1
            for j in range(len(data_x)):
                if j != i:
                    af *= (1.0 * (testdata - data_x[j]) / (data_x[i] - data_x[j]))
            predict += data_y[i] * af
    return predict


# 更改参数，方便使用
def plot(data, nums, fun, title):
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]

    Area = [min(data_x), max(data_x)]

    X = [Area[0] + 1.0 * i * (Area[1] - Area[0]) / nums for i in range(nums)]
    X[len(X) - 1] = Area[1]

    Y = [fun(data, x) for x in X]

    plt.plot(X, Y, label='result')
    plt.plot(data_x, data_y, 'ro', label='point')
    plt.xlabel('X_value')
    plt.ylabel('Y_value')
    plt.title(title)
    plt.show()


print('\n物体一在-3.75的预测值：', round(Lg(data1, -3.75), 3))
print('物体一在0.25的预测值：', round(Lg(data1, 0.25), 3))
print('物体二在-3.75的预测值：', round(Lg(data2, -3.75), 3))
print('物体二在0.25的预测值：', round(Lg(data2, 0.25), 3))
plot(data1, 20, Lg, 'La_1')
plot(data2, 20, Lg, 'La_2')

# MSE误差分析
MSE1 = (pow(y_1_real - Lg(data1, -3.75), 2) + pow(y_2_real - Lg(data1, 0.25), 2)) / 2
MSE2 = (pow(y_3_real - Lg(data2, -3.75), 2) + pow(y_4_real - Lg(data2, 0.25), 2)) / 2

print("物体一的误差为：", round(MSE1, 3))
print("物体二的误差为：", round(MSE2, 3))


# 2
# 算法部分
def DivideLine(data, testdata):
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]

    if testdata in data_x:
        return data_y[data_x.index(testdata)]
    else:
        index = 0
        for j in range(len(data_x)):
            if data_x[j] < testdata < data_x[j + 1]:
                index = j
                break
        predict = 1.0 * (testdata - data_x[j]) * (data_y[j + 1] - data_y[j]) / (data_x[j + 1] - data_x[j]) + data_y[j]
        return predict


# 预测结果
print('\n物体一在-3.75的预测值：', round(DivideLine(data1, -3.75), 3))
print('物体一在0.25的预测值：', round(DivideLine(data1, 0.25), 3))
print('物体二在-3.75的预测值：', round(DivideLine(data2, -3.75), 3))
print('物体二在0.25的预测值：', round(DivideLine(data2, 0.25), 3))
plot(data1, 20, DivideLine, 'DivideLine_1')
plot(data2, 20, DivideLine, 'DivideLine_2')

# MSE误差分析
MSE1 = (pow(y_1_real - DivideLine(data1, -3.75), 2) + pow(y_2_real - DivideLine(data1, 0.25), 2)) / 2
MSE2 = (pow(y_3_real - DivideLine(data2, -3.75), 2) + pow(y_4_real - DivideLine(data2, 0.25), 2)) / 2

print("物体一的误差为：", round(MSE1, 3))
print("物体二的误差为：", round(MSE2, 3))


# 3
def calF(data):
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]
    F = [1 for i in range(len(data))]
    FM = []
    for i in range(len(data)):
        FME = []
        if i == 0:
            FME = data_y
        else:
            for j in range(len(FM[len(FM) - 1]) - 1):
                delta = data_x[i + j] - data_x[j]
                value = 1.0 * (FM[len(FM) - 1][j + 1] - FM[len(FM) - 1][j]) / delta
                FME.append(value)
        FM.append(FME)
    F = [fme[0] for fme in FM]
    # print(FM)
    return F


def NT(data, testdata, F):
    predict = 0
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]
    if testdata in data_x:
        return data_y[data_x.index(testdata)]
    else:
        for i in range(len(data_x)):
            Eq = 1
            if i != 0:
                for j in range(i):
                    Eq = Eq * (testdata - data_x[j])
                predict += (F[i] * Eq)
    return predict


def plot(data, nums, title):
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]

    Area = [min(data_x), max(data_x)]

    X = [Area[0] + 1.0 * i * (Area[1] - Area[0]) / nums for i in range(nums)]
    X[len(X) - 1] = Area[1]

    F = calF(data)
    Y = [NT(data, x, F) for x in X]

    plt.plot(X, Y, label='result')
    plt.plot(data_x, data_y, 'ro', label='point')
    plt.title(title)
    plt.show()


print('\n物体一在-3.75的预测值：', round(NT(data1, -3.75, calF(data1)), 3))
print('物体一在0.25的预测值：', round(NT(data1, 0.25, calF(data1)), 3))
print('物体二在-3.75的预测值：', round(NT(data2, -3.75, calF(data2)), 3))
print('物体二在0.25的预测值：', round(NT(data2, 0.25, calF(data2)), 3))
plot(data1, 20, 'NT_1')
plot(data2, 20, 'NT_2')

# 4
# 生成X、Y数据
x = [data1[i][0] for i in range(len(data1))]
y1 = [data1[i][1] for i in range(len(data1))]
y2 = [data2[i][1] for i in range(len(data2))]

# 物体一
# 标签
xnew = np.linspace(-5, 5, 21)
pl.plot(x, y1, "ro")
for kind in ["linear", "quadratic", "cubic"]:
    f1 = interpolate.interp1d(x, y1, kind=kind)
    ynew = f1(xnew)
    pl.plot(xnew, ynew, label=str(kind))

# 预测
print('\n物体一在-3.75的预测值：%.3f' % f1(-3.75))
print('物体一在0.25的预测值：%.3f' % f1(0.25))

# 增加内容
f4 = interpolate.splrep(x, y1)
ynew4 = interpolate.splev(xnew, f4, der=0)
pl.plot(xnew, ynew4, label=str("cubic spline"))
pl.legend(loc="lower right")
plt.xlabel('X_value')
plt.ylabel('Y_value')
plt.title('4.1')
pl.show()

# 物体二
pl.plot(x, y2, "ro")
for kind in ["linear", "quadratic", "cubic"]:
    f2 = interpolate.interp1d(x, y2, kind=kind)
    ynew = f2(xnew)
    pl.plot(xnew, ynew, label=str(kind))

# 预测
print('物体二在-3.75的预测值：%.3f' % f2(-3.75))
print('物体二在0.25的预测值：%.3f' % f2(0.25))

f4 = interpolate.splrep(x, y2)
ynew4 = interpolate.splev(xnew, f4, der=0)
pl.plot(xnew, ynew4, label=str("cubic spline"))
pl.legend(loc="lower right")
plt.xlabel('X_value')
plt.ylabel('Y_value')
plt.title('4.2')
pl.show()


# MSE误差分析
MSE1 = (pow(y_1_real - f1(-3.75), 2) + pow(y_2_real - f1(0.25), 2)) / 2
MSE2 = (pow(y_3_real - f2(-3.75), 2) + pow(y_4_real - f2(0.25), 2)) / 2

print("物体一的误差为：", round(MSE1, 3))
print("物体二的误差为：", round(MSE2, 3))