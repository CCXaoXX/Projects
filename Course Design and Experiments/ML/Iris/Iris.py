from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


###############################################################
# 训练部分，包括内核选择、预处理、准确率

x_data = datasets.load_iris().data
y_data = datasets.load_iris().target
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, random_state=166, train_size=0.6)
'''训练测试3:2，shuffle数据。'''


lin_svc = svm.SVC(decision_function_shape='ovo', kernel='linear', C=0.2)  # 线性
lin_svc.fit(x_train, y_train.ravel())
poly_svc = svm.SVC(decision_function_shape='ovo', kernel='poly', C=0.2)  # 偏线性
poly_svc.fit(x_train, y_train.ravel())
rbf_svc = svm.SVC(decision_function_shape='ovo', kernel='rbf', C=0.2)  # 偏非线性
rbf_svc.fit(x_train, y_train.ravel())
sigmoid_svc = svm.SVC(decision_function_shape='ovo', kernel='sigmoid', C=0.2)  # 非线性
sigmoid_svc.fit(x_train, y_train.ravel())
linear = svm.LinearSVC(C=0.2)  # 线性
linear.fit(x_train, y_train.ravel())
'''C接近0，防止过拟合，提高泛化性'''


print('acc:')
print('lin_svc:', lin_svc.score(x_test, y_test))
print('poly_svc:', poly_svc.score(x_test, y_test))
print('rbf_svc:', rbf_svc.score(x_test, y_test))
print("线性ovr核:", linear.score(x_test, y_test))
print('sigmoid_svc', sigmoid_svc.score(x_test, y_test))
'''可以看到svm的线性内核效果很好，且对于iris，ovo效果会好一些。
样本多，特征多，二分类，选择线性核函数
样本多，特征多，多分类，多项式核函数
样本不多，特征多，二分类/多分类，高斯核函数
样本不多，特征不多，二分类/多分类，高斯核函数
'''


###############################################################
# 画图部分,x特征只能选取两个，所以准确率并没有上半部分高，只是为了结果可视化。
# plot
X = x_data[:, :2]  # 只取前两维特征
y = y_data

h = .02  # 网格中的步长

# 创建支持向量机实例，并拟合出数据
svc = lin_svc.fit(X, y)  # 线性核
rbf_svc = rbf_svc.fit(X, y)  # 径向基核
poly_svc = poly_svc.fit(X, y)  # 多项式核
lin_svc = linear.fit(X, y)  # 线性核

# 创建网格，以绘制图像
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# 图的标题
titles = ['SVC with linear kernel',
          'LinearSVC (linear kernel)',
          'SVC with RBF kernel',
          'SVC with polynomial (degree 3) kernel']

for i, clf in enumerate((svc, lin_svc, rbf_svc, poly_svc)):
    # 绘出决策边界，不同的区域分配不同的颜色
    plt.subplot(2, 2, i + 1)  # 创建一个2行2列的图，并以第i个图为当前图
    plt.subplots_adjust(wspace=0.4, hspace=0.4)  # 设置子图间隔

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])  # 将xx和yy中的元素组成一对对坐标，作为支持向量机的输入，返回一个array

    # 把分类结果绘制出来
    Z = Z.reshape(xx.shape)  # (220, 280)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)  # 使用等高线的函数将不同的区域绘制出来

    # 将训练数据以离散点的形式绘制出来
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])

plt.show()
