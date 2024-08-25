import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.metrics import r2_score
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np

data_train = pd.read_csv("./train.csv")
data_test = pd.read_csv("./test.csv")
data_test_sample = pd.read_csv("./sample_submission.csv")

# spilt
cols = ['OverallQual','GrLivArea', 'FullBath', 'TotRmsAbvGrd', 'YearBuilt']
# cols = ['MSSubClass', 'LotArea', 'OverallQual', 'OverallCond', 'YearRemodAdd', '1stFlrSF', '2ndFlrSF',
# 'GrLivArea', 'YrSold', 'YearBuilt']

x_train = data_train[cols].values
y_train = data_train['SalePrice'].values
x_train = preprocessing.StandardScaler().fit_transform(x_train)

x_test = data_test[cols].values
y_test = data_test_sample['SalePrice'].values
x_test = preprocessing.StandardScaler().fit_transform(x_test)

#  test
clf = GradientBoostingRegressor()
clf.fit(x_train, y_train)
y_pre = clf.predict(x_test)

#  验证指标
print("acc：", 1 - r2_score(y_true=y_pre, y_pred=y_test))

# save file
prediction = pd.DataFrame(y_pre, columns=['SalePrice'])
result = pd.concat([data_test['Id'], prediction], axis=1)
result.to_csv('./result_train.csv', index=False)

#  Error plot
image = sns.lineplot(x=data_test['Id'], y=y_pre)
image.legend('real')
image = sns.lineplot(x=data_test['Id'], y=y_test)
image.legend('predict')
sns.scatterplot(x=data_test['Id'], y=y_pre)
sns.scatterplot(x=data_test['Id'], y=y_test)
image.set_ylabel('SalePrice')
image.set_title('Error plot')
plt.show()
