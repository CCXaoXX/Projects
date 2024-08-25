import copy


class node(object):
    def __init__(self, start, end, length, state=1, ID=0):
        self.start = start  # 起始地址
        self.end = end  # 结束地址
        self.length = length # 内存大小
        self.state = state  # state为1：内存未分配
        self.Id = ID  # ID为0是未分配，其余为任务编号


def showList(list):
    """展示空闲分区"""
    print("空闲分区如下")
    id = 1
    for i in range(0, len(list)):
        p = list[i]
        if p.state == 1:
            print(id, ' :起始地址 ', p.start, " 结束地址 ", p.end, " 长度 ", p.length)
            id += 1


def showList_busy(list):
    """展示已分配分区"""
    print("已分配分区如下")
    for i in range(0, len(list)):
        p = list[i]
        if p.state == 0:
            print(p.Id, ' :起始地址 ', p.start, " 结束地址 ", p.end, " 长度 ", p.length)


def free_k(taskID, li):
    for i in range(0, len(li)):
        p = li[i]
        if p.Id == taskID:
            p.state = 1
            x = i
            print("已释放", taskID, ' :起始地址 ', p.start, " 结束地址 ", p.end, " 长度 ", p.length)
            break

    # 向前合并空闲块
    if x - 1 > 0:
        if li[x - 1].state == 1:
            a = node(li[x - 1].start, li[x].end, li[x - 1].length + li[x].length, 1, 0)
            del li[x - 1]
            del li[x - 1]
            li.insert(x - 1, a)
            x = x - 1
    # 向后合并空闲块
    if x + 1 < len(li):
        if li[x + 1].state == 1:
            a = node(li[x].start, li[x + 1].end, li[x].length + li[x + 1].length, 1, 0)
            del li[x]
            del li[x]
            li.insert(x, a)
    showList(li)


# 首次适应算法
def FF(taskID, Tasklength, list):
    for i in range(0, len(list)):
        p = list[i]
        if p.state == 1 and p.length > Tasklength:
            node2 = node(p.start + Tasklength, p.end, p.length - Tasklength, 1, 0)
            a = node(p.start, p.start + Tasklength - 1, Tasklength, state=0, ID=taskID)
            print("已分配\n", a.Id, ' :起始地址 ', a.start, " 结束地址 ", a.end, " 长度 ", a.length)
            del list[i]
            list.insert(i, node2)
            list.insert(i, a)
            # showList(list)
            return
        if p.state == 1 and p.length == Tasklength:
            print("已分配\n", taskID, ' :起始地址 ', p.start, " 结束地址 ", p.end, " 长度 ", p.length)
            p.state = 0
            showList(list)
            return
    print("内存空间不足")


# 循环首次适应算法
def NF(taskID, Tasklength, list):
    global p_sign, p_num, time
    if time == 0:
        p_sign = list[0]
        time = 1
    for i in range(0, len(list)):
        p = list[i]
        if (p.start - 1) == p_sign.end:
            p_num = i
    for i in range(p_num, len(list)):
        p = list[i]
        if p.state == 1 and p.length > Tasklength:
            node2 = node(p.start + Tasklength, p.end, p.length - Tasklength, 1, 0)
            a = node(p.start, p.start + Tasklength - 1, Tasklength, state=0, ID=taskID)
            print("已分配\n", a.Id, ' :起始地址 ', a.start, " 结束地址 ", a.end, " 长度 ", a.length)
            p_sign = a
            del list[i]
            list.insert(i, node2)
            list.insert(i, a)
            # showList(list)
            return
        if p.state == 1 and p.length == Tasklength:
            print("已分配\n", taskID, ' :起始地址 ', p.start, " 结束地址 ", p.end, " 长度 ", p.length)
            p.state = 0
            showList(list)
            return
    for i in range(p_num):
        p = list[i]
        if p.state == 1 and p.length > Tasklength:
            node2 = node(p.start + Tasklength, p.end, p.length - Tasklength, 1, 0)
            a = node(p.start, p.start + Tasklength - 1, Tasklength, state=0, ID=taskID)
            p_sign = a
            del list[i]
            list.insert(i, node2)
            list.insert(i, a)
            showList(list)
            return
        if p.state == 1 and p.length == Tasklength:
            p.state = 0
            showList(list)
            return
    print("内存空间不足")


# 最佳适应算法
def bubble_sort(list):
    # 冒泡排序
    count = len(list)
    for i in range(0, count):
        for j in range(i + 1, count):
            if list[i].length < list[j].length:
                list[i], list[j] = list[j], list[i]
    return list


def BF(taskID, Tasklength, li):
    q = copy.copy(li)
    q = bubble_sort(q)
    s = -1
    ss12 = -1
    for i in range(0, len(q)):
        p = q[i]
        if p.state == 1 and p.length > Tasklength:
            s = p.start
        elif p.state == 1 and p.length == Tasklength:
            ss12 = p.start
    if s == -1 and ss12 == -1:
        print("内存空间不足")
        return
    for i in range(0, len(li)):
        p = li[i]
        if p.start == s:
            node2 = node(p.start + Tasklength, p.end, p.length - Tasklength, 1, 0)
            a = node(p.start, p.start + Tasklength - 1, Tasklength, state=0, ID=taskID)
            print("已分配\n", a.Id, ' :起始地址 ', a.start, " 结束地址 ", a.end, " 长度 ", a.length)
            del li[i]
            li.insert(i, node2)
            li.insert(i, a)
            # showList(li)
            return
        elif p.start == ss12:
            print("已分配\n", taskID, ' :起始地址 ', p.start, " 结束地址 ", p.end, " 长度 ", p.length)
            p.state = 0
            showList(li)
            return


# 最坏适应算法
def bubble_sort2(list):
    # 冒泡排序
    count = len(list)
    for i in range(0, count):
        for j in range(i + 1, count):
            if list[i].length > list[j].length:
                list[i], list[j] = list[j], list[i]
    return list


def WF(taskID, Tasklength, li):
    q = copy.copy(li)
    q = bubble_sort2(q)
    s = -1
    ss12 = -1
    for i in range(0, len(q)):
        p = q[i]
        if p.state == 1 and p.length > Tasklength:
            s = p.start
        elif p.state == 1 and p.length == Tasklength:
            ss12 = p.start
    if s == -1 and ss12 == -1:
        print("内存空间不足")
        return
    for i in range(0, len(li)):
        p = li[i]
        if p.start == s:
            node2 = node(p.start + Tasklength, p.end, p.length - Tasklength, 1, 0)
            a = node(p.start, p.start + Tasklength - 1, Tasklength, state=0, ID=taskID)
            print("已分配\n", a.Id, ' :起始地址 ', a.start, " 结束地址 ", a.end, " 长度 ", a.length)
            del li[i]
            li.insert(i, node2)
            li.insert(i, a)
            # showList(li)
            return
        elif p.start == ss12:
            print("已分配\n", taskID, ' :起始地址 ', p.start, " 结束地址 ", p.end, " 长度 ", p.length)
            p.state = 0
            showList(li)
            return


def main():
    x = int(input("请选择操作:\n0\t首次适应算法\n1\t循环首次适应算法\n2\t最佳适应算法\n3\t最坏适应算法\n4\t退出程序\n"))
    a = node(0, 639, 640, state=1, ID=0)
    b = []
    b.append(a)
    if x == 0:
        auto_num1 = int(input("请选择操作:\n0\t运行示例\n1\t手动分配内存\n"))
        FF('OS', 40, b)
        if auto_num1 == 0:
            FF(1, 130, b)
            FF(2, 60, b)
            FF(3, 100, b)
            showList_busy(b)
            free_k(2, b)
            FF(4, 200, b)
            showList_busy(b)
            free_k(3, b)
            free_k(1, b)
            showList_busy(b)
            FF(5, 140, b)
            FF(6, 60, b)
            FF(7, 50, b)
            showList_busy(b)
        while True and auto_num1:
            print("")
            sele_0 = int(input("请选择操作:\n1\t分配内存\n2\t释放分区\n3\t展示空闲分区表\n4\t展示已分配分区表\n5\t退出程序\n"))
            if sele_0 == 1:
                db_id = int(input("请输入要分配任务的ID:\n"))
                id_size = int(input("请输入要该任务需要的内存大小:\n"))
                FF(db_id, id_size, b)
            elif sele_0 == 2:
                fr_id = int(input("请输入要释放任务的ID:\n"))
                free_k(fr_id, b)
            elif sele_0 == 3:
                showList(b)
            elif sele_0 == 4:
                showList_busy(b)
            elif sele_0 == 5:
                break
            else:
                print("请重新输入")
    elif x == 1:
        auto_num1 = int(input("请选择操作:\n0\t运行示例\n1\t手动分配内存\n"))
        NF('OS', 40, b)
        if auto_num1 == 0:
            NF(1, 130, b)
            NF(2, 60, b)
            NF(3, 100, b)
            free_k(2, b)
            NF(4, 200, b)
            free_k(3, b)
            free_k(1, b)
            NF(5, 140, b)
            NF(6, 60, b)
            NF(7, 50, b)
            showList_busy(b)
        while True and auto_num1:
            print("")
            sele_0 = int(input("请选择操作:\n1\t分配内存\n2\t释放分区\n3\t展示空闲分区表\n4\t展示已分配分区表\n5\t退出程序\n"))
            if sele_0 == 1:
                db_id = int(input("请输入要分配任务的ID:\n"))
                id_size = int(input("请输入要该任务需要的内存大小:\n"))
                NF(db_id, id_size, b)
            elif sele_0 == 2:
                fr_id = int(input("请输入要释放任务的ID:\n"))
                free_k(fr_id, b)
            elif sele_0 == 3:
                showList(b)
            elif sele_0 == 4:
                showList_busy(b)
            elif sele_0 == 5:
                break
            else:
                print("请重新输入")
    elif x == 2:
        auto_num1 = int(input("请选择操作:\n0\t运行示例\n1\t手动分配内存\n"))
        BF('OS', 40, b)
        if auto_num1 == 0:
            BF(1, 130, b)
            BF(2, 60, b)
            BF(3, 100, b)
            free_k(2, b)
            BF(4, 200, b)
            free_k(3, b)
            free_k(1, b)
            BF(5, 140, b)
            BF(6, 60, b)
            BF(7, 50, b)
            showList_busy(b)
        while True and auto_num1:
            print("")
            sele_0 = int(input("请选择操作:\n1\t分配内存\n2\t释放分区\n3\t展示空闲分区表\n4\t展示已分配分区表\n5\t退出程序\n"))
            if sele_0 == 1:
                db_id = int(input("请输入要分配任务的ID:\n"))
                id_size = int(input("请输入要该任务需要的内存大小:\n"))
                BF(db_id, id_size, b)
            elif sele_0 == 2:
                fr_id = int(input("请输入要释放任务的ID:\n"))
                free_k(fr_id, b)
            elif sele_0 == 3:
                showList(b)
            elif sele_0 == 4:
                showList_busy(b)
            elif sele_0 == 5:
                break
            else:
                print("请重新输入")
    elif x == 3:
        auto_num1 = int(input("请选择操作:\n0\t运行示例\n1\t手动分配内存\n"))
        WF('OS', 40, b)
        if auto_num1 == 0:
            WF(1, 130, b)
            WF(2, 60, b)
            WF(3, 100, b)
            free_k(2, b)
            WF(4, 200, b)
            free_k(3, b)
            free_k(1, b)
            WF(5, 140, b)
            WF(6, 60, b)
            WF(7, 50, b)
            showList_busy(b)
        while True and auto_num1:
            print("")
            sele_0 = int(input("请选择操作:\n1\t分配内存\n2\t释放分区\n3\t展示空闲分区表\n4\t展示已分配分区表\n5\t退出程序\n"))
            if sele_0 == 1:
                db_id = int(input("请输入要分配任务的ID:\n"))
                id_size = int(input("请输入要该任务需要的内存大小:\n"))
                WF(db_id, id_size, b)
            elif sele_0 == 2:
                fr_id = int(input("请输入要释放任务的ID:\n"))
                free_k(fr_id, b)
            elif sele_0 == 3:
                showList(b)
            elif sele_0 == 4:
                showList_busy(b)
            elif sele_0 == 5:
                break
            else:
                print("请重新输入")
    elif x == 4:
        return
    else:
        print("输入错误")


if __name__ == "__main__":
    try:
        p_sign = None
        p_num = 0
        time = 0
        main()
        input('键入以离开')
    except:
        print("输入错误")
        input('键入以离开')