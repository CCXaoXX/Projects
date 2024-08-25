#KochDrawV1.py
import turtle as t
def koch(size,n):
    if n == 0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(size/3,n-1)
def main(level):
    t.setup(600,600)
    t.penup()
    t.goto(-200,100)
    t.pendown()
    t.pensize(2)
    koch(400,level)
    t.right(120)
    koch(400,level)
    t.right(120)
    koch(400,level)
    t.hideturtle()
    t.done()
try:
    level = eval(input("请输入科赫曲线的阶数："))
    main(level)
except:
    print("输入错误")
