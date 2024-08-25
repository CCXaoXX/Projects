#WeekNamePrintV2.py
weekStr = "一二三四五六日"
weekId = eval(input("请输入星期数字(1-7)："))
if weekId in [1,2,3,4,5,6,7]:
    print("星期"+weekStr[weekId-1])
else:
    print("输入错误")
