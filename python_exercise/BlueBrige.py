import os
import sys

# 请在此输入您的代码
m = int(input())
n = int(input())

ans = {}
for i in range(1, m + 1):
    if i < 10:
        ans[i] = [i]
    else:
        summ = 0
        temp = i
        while temp:
            summ += temp % 10
            temp //= 10
        if summ in ans:
            ans[summ].append(i)
        else:
            ans[summ] = [i]

flag = 0
for i in ans:
    for j in ans[i]:
        if n - 1 > 0:
            n -= 1
        else:
            print(j)
            flag = 1
            break
    if flag == 1:
        break
