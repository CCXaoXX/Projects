import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression

x_fearures = np.array([[-1, -2], [-2, -1], [-3, -2], [1, 3], [2, 1], [3, 2]])
y_label = np.array([0, 0, 0, 1, 1, 1])
lr_clf = LogisticRegression()
lr_clf = lr_clf.fit(x_fearures, y_label)

print('the weight of Logistic Regression:', lr_clf.coef_)
print('the intercept(w0) of Logistic Regression:', lr_clf.intercept_)

plt.figure()
plt.scatter(x_fearures[:, 0], x_fearures[:, 1], c = y_label, s = 50, cmap= 'viridis')
plt.title('Dataset')

nx, ny = 200, 100
x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()
x_grid, y_grid = np.meshgrid(np.linspace(x_min, x_max, nx), np.linspace(y_min, y_max, ny))

z_proba = lr_clf.predict_proba(np.c_[x_grid.ravel(), y_grid.ravel()])
z_proba = z_proba[:, 1].reshape(x_grid.shape)
plt.contour(x_grid, y_grid, z_proba, [0.5], linewidths =2., colors = 'blue')

plt.show()