import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']


# 3
def lstsq(A, b):
    b = b.T
    x = np.linalg.lstsq(A, b, rcond=None)
    print('x0:', round(x[0].item(0), 3))
    print('x1:', round(x[0].item(1), 3))
    return x


a = np.mat([[2, 4], [3, -5], [1, 2], [2, 1]])
b = np.mat([11, 3, 6, 7])

lstsq(a, b)


# 4
x = np.mat([[1, 0], [0, 1], [1, 1]])
y = np.mat([4, 2, 6.5])

lstsq(x, y)


# 6
def fun(x, c0, c1):
    return x / (c0 * x + c1)


x = [1, 2, 4, 5]
y = [0.33, 0.40, 0.44, 0.45]
x = np.array(x)
y = np.array(y)

popt, pcov = curve_fit(fun, x, y)

c0 = popt[0]
c1 = popt[1]
yvals = fun(x, c0, c1)

print('系数c0:', round(c0, 3))
print('系数c1:', round(c1, 3))
print('参数的协方差为:\n', pcov)

fig = plt.figure(figsize=(10, 7))
plot1 = plt.plot(x, y, 's', label='真实值')
plot2 = plt.plot(x, yvals, 'r', label='拟合曲线')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')
plt.title('拟合图')
plt.show()
