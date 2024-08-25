import scipy.signal
import numpy as np
import torch

input1 = [[2, 7, 3],
          [5, 8, 1],
          [9, 2, 8]]
input2 = [[0, -1, 0],
          [-1, 4, -1],
          [0, -1, 0]]
result1 = scipy.signal.convolve(input1, input2)
result2 = scipy.signal.convolve(input1, input2, mode='same')
result3 = scipy.signal.convolve(input1, input2, mode='valid')
print(result1)
print(result2)
print(result3)

RGB = np.array([100, 98, 200]).reshape([3, 1])
a = np.array([[1, 0, 1.14],
                  [1, -0.395, -0.581],
                  [1, 2.032, 0]])
b = np.array([[0.299, 0.587, 0.114],
                  [-0.148, -0.289, 0.437],
                  [0.615, -0.515, -0.1]])
print(b)
YUV = np.matmul(b, RGB)
print(YUV)

YUV[0] *= 1.1
print(YUV)

print(np.matmul(a, YUV))
