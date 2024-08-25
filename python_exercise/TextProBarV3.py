#TextProBarV3.py
import time
scale = 100
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()
for i in range(scale+1):
    if i < 11:
        a = '*' * i
        b = '.' * (scale - i)
        c = (i / scale) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]用时{:.2f}s".format(c, a, b, dur), end="")
        time.sleep((1 + (1 - 0.1) ** 1.5) - 1)
    else:
        a = '*' * i
        b = '.' * (scale - i)
        c = (i / scale) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]用时{:.2f}s".format(c, a, b, dur), end="")
        time.sleep((0.1 + (1 - 0.5) * 0.01) ** 1.1)
print("\n"+"执行结束".center(scale//2,'-'))