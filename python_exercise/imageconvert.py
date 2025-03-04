from PIL import Image
import numpy as np

a = np.asarray(Image.open('C:\Users\86159\OneDrive\图片\屏幕快照\convert.png').convert('L')).astype('float')

depth = 10.
grad = np.gradient(a)
grad_x, grad_y = grad
grad_x = grad_x * depth / 100
grad_y = grad_y * depth / 100
A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1)
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1. / A

vec_el = np.pi / 2.2
vec_az = np.pi / 4
dx = np.cos(vec_el) * np.cos(vec_az)
dy = np.cos(vec_el) * np.sin(vec_az)
dz = np.sin(vec_el)

b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)
b = b.clip(0, 255)
im = Image.fromarray(b.astype('uint8'))
try:
    im.save('C:\Users\86159\OneDrive\图片\屏幕快照\emp.png')
    print('转化成功')
except:
    print('转化失败')