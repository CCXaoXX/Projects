# coding: utf-8

import numpy as np
import mindspore.nn as nn
import mindspore.ops as ops
from mindspore import Tensor
from mindspore import ParameterTuple, Parameter
from mindspore import dtype as mstype


class Net(nn.Cell):
    def __init__(self):
        super(Net, self).__init__()
        self.matmul = ops.MatMul()  # 创建了一个矩阵乘法操作对象
        self.z = Parameter(Tensor(np.array([1.0, 1.0, 1.0], np.float32)), name='z')  # 创建一个参数对象

    def construct(self, x, y):
        x = x * self.z
        out = self.matmul(x, y)
        return out
    

model = Net()  # 创建一个Net的实例model

for m in model.parameters_and_names():
    print(m)

x = Tensor([[0.8, 0.6, 0.2], [1.8, 1.3, 1.1]], dtype=mstype.float32)  # 创建Tensor类型的输入数据
y = Tensor([[0.11, 3.3, 1.1], [1.1, 0.2, 1.4], [1.1, 2.2, 0.3]], dtype=mstype.float32)
result = model(x, y)
print(result)