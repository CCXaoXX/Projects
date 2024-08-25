import random
import copy


class PCB:
    """表示一个进程块"""

    def __init__(self, pid, priority, in_time, need_time):  # 初始化进程
        self.pid = pid  # 进程pid
        self.priority = priority  # 进程优先级
        self.dy_priority = priority  # 进程动态优先级
        self.alter_time = 999  # 进程优先级上次修改时间
        self.in_time = in_time  # 进程进入内存时间
        self.start_time = 999  # 进程开始运行时间
        self.need_time = need_time  # 进程需要运行时间
        self.cpu_time = 0  # 进程已运行(服务)时间
        self.remain_time = need_time  # 进程剩余运行时间
        self.out_time = 999  # 进程运行结束时间
        self.turn_time = 999  # 进程周转时间
        self.Wturn_time = 999  # 进程带权周转时间
        self.fir = 0  # 进程是否为第一次进入内存

    def ch_output(self):  # 运行前进程表
        print("进程" + str(self.pid), "优先级:" + str(self.priority), "进入内存时间:" +
              str(self.in_time), "需要运行时间:" + str(self.need_time))

    def i_output(self):  # 运行过程中进程表
        print("进程" + str(self.pid),
              "需要运行时间:" + str(self.need_time),
              "已经运行时间:" + str(self.cpu_time))

    def hpf_output(self):
        print("进程" + str(self.pid),
              "优先级:" + str(self.dy_priority),
              "需要运行时间:" + str(self.need_time),
              "已经运行时间:" + str(self.cpu_time))

    def over_output(self):  # 运行结束后进程表
        print("进程" +
              str(self.pid) +
              "\t" +
              "优先级:" +
              str(self.priority) +
              "\t" +
              "进入内存时间:" +
              str(self.in_time) +
              "\t" +
              "开始运行时间:" +
              str(self.start_time) +
              "\t" +
              "需要运行时间:" +
              str(self.need_time) +
              "\t" +
              "已经运行时间:" +
              str(self.cpu_time) +
              "\t" +
              "运行结束时间:" +
              str(self.out_time) +
              "\t" +
              "进程周转时间:" +
              str(self.turn_time) +
              "\t" +
              "进程带权周转时间:" +
              "%2.2f" % self.Wturn_time
              )


def init(num):  # 初始化进程，生成四个进程并按到达时间将它们放入列表list1
    pcb_list = []
    for i in range(num):
        # 进程号      进程优先级          进程进入内存时间      进程需要运行时间
        pcb_list.append(PCB(str(i), random.randint(1, 9),
                            random.randint(0, 10), random.randint(1, 6)))
    for i in range(len(pcb_list) - 1):
        for j in range(i + 1, len(pcb_list)):
            if pcb_list[i].in_time > pcb_list[j].in_time:
                pcb_list[i], pcb_list[j] = pcb_list[j], pcb_list[i]
    return pcb_list


def record_pcb(num):
    pcb_list = []
    for i in range(num):
        # 进程号      进程优先级          进程进入内存时间      进程需要运行时间
        a = int(input("请输入%d号进程的优先级：" % i))
        b = int(input("请输入%d号进程进入内存时间：" % i))
        c = int(input("请输入%d号进程需要运行的时间：" % i))
        pcb_list.append(PCB(str(i), a, b, c))
    for i in range(len(pcb_list) - 1):
        for j in range(i + 1, len(pcb_list)):
            if pcb_list[i].in_time > pcb_list[j].in_time:
                pcb_list[i], pcb_list[j] = pcb_list[j], pcb_list[i]
    return pcb_list


def sort_list(pcb_list):
    for i in range(len(pcb_list) - 1):
        for j in range(i + 1, len(pcb_list)):
            if pcb_list[i].pid > pcb_list[j].pid:
                pcb_list[i], pcb_list[j] = pcb_list[j], pcb_list[i]
    for i in pcb_list:
        if i.start_time == 999:
            i.ch_output()
        else:
            i.over_output()
    print("")
    return pcb_list


def SP(pcb_list):
    """静态高优先级优先"""
    time = 0
    AV_turn = 0
    AV_Wturn = 0
    list2 = []  # 运行完毕的进程组
    min_time = 999
    run_pcb = 1

    def SP_sort(p_list):
        # 将就绪队列按进程长度从小到大排列
        ready_num = 0
        for i in p_list:
            if time >= i.in_time:
                ready_num += 1
                if i.need_time < min_time:
                    temp = i
                    p_list.remove(i)
                    p_list.insert(0, temp)
        if ready_num > 1:  # 解决后来者居上的bug
            for k in range(ready_num - 1):
                for j in range(k + 1, ready_num):
                    if pcb_list[k].priority < pcb_list[j].priority:
                        pcb_list[k], pcb_list[j] = pcb_list[j], pcb_list[k]
        return p_list

    while pcb_list:
        print("time:", time)
        if run_pcb == 0:  # 当前没有进程执行时，就将就绪队列按进程长度从小到大排列
            pcb_list = SP_sort(pcb_list)
        if time >= pcb_list[0].in_time:
            run_pcb = 1
            if pcb_list[0].fir == 0:
                print("进程" + str(pcb_list[0].pid) + "开始运行")
                pcb_list[0].start_time = time
                pcb_list[0].fir = 1
            pcb_list[0].cpu_time += 1
            pcb_list[0].hpf_output()
            if pcb_list[0].need_time == pcb_list[0].cpu_time:
                print("进程" + str(pcb_list[0].pid) + "运行结束")
                pcb_list[0].out_time = time + 1
                pcb_list[0].turn_time = pcb_list[0].out_time - \
                                        pcb_list[0].in_time
                pcb_list[0].Wturn_time = pcb_list[0].turn_time / \
                                         pcb_list[0].need_time
                list2.append(pcb_list[0])
                pcb_list.remove(pcb_list[0])
                run_pcb = 0
                # pcb_list = Sjf_sort(pcb_list)
        time += 1
    for i in list2:
        AV_turn += i.turn_time  # 计算平均周转时间
        AV_Wturn += i.Wturn_time  # 计算平均带权周转时间
    print("\r")
    print(
        "\t" * 4 + "静态高优先级优先算法 平均周转时间为:%2.2f,平均带权周转时间为:%2.2f" %
        (AV_turn / 4, AV_Wturn / 4))
    return list2


def DP(pcb_list):
    """动态高优先级优先"""
    time = 0
    AV_turn = 0
    AV_Wturn = 0
    list2 = []  # 运行完毕的进程组
    min_time = 999
    run_pcb = 1

    def DP_sort(p_list):
        # 将就绪队列按进程长度从小到大排列
        ready_num = 0
        for i in p_list:
            if time >= i.in_time:
                ready_num += 1
                if i.need_time < min_time:
                    temp = i
                    p_list.remove(i)
                    p_list.insert(0, temp)
        if ready_num > 1:  # 解决后来者居上的bug
            for k in range(ready_num - 1):
                for j in range(k + 1, ready_num):
                    if pcb_list[k].dy_priority < pcb_list[j].dy_priority:
                        pcb_list[k], pcb_list[j] = pcb_list[j], pcb_list[k]
                    elif (pcb_list[k].dy_priority == pcb_list[j].dy_priority) and (
                            pcb_list[k].alter_time < pcb_list[j].alter_time):
                        pcb_list[k], pcb_list[j] = pcb_list[j], pcb_list[k]
        return p_list

    while pcb_list:
        print("time:", time)
        # 当前没有进程执行时，就将就绪队列按进程长度从小到大排列
        pcb_list = DP_sort(pcb_list)
        if time >= pcb_list[0].in_time:
            run_pcb = 1
            if pcb_list[0].fir == 0:
                print("进程" + str(pcb_list[0].pid) + "开始运行")
                pcb_list[0].start_time = time
                pcb_list[0].fir = 1
            pcb_list[0].cpu_time += 1
            if pcb_list[0].dy_priority:  # 使进程的优先级不会变为负数
                pcb_list[0].dy_priority -= 1
            pcb_list[0].alter_time = time
            pcb_list[0].hpf_output()
            if pcb_list[0].need_time == pcb_list[0].cpu_time:
                print("进程" + str(pcb_list[0].pid) + "运行结束")
                pcb_list[0].out_time = time + 1
                pcb_list[0].turn_time = pcb_list[0].out_time - \
                                        pcb_list[0].in_time
                pcb_list[0].Wturn_time = pcb_list[0].turn_time / \
                                         pcb_list[0].need_time
                list2.append(pcb_list[0])
                pcb_list.remove(pcb_list[0])
                run_pcb = 0
                # pcb_list = Sjf_sort(pcb_list)
        time += 1
    for i in list2:
        AV_turn += i.turn_time  # 计算平均周转时间
        AV_Wturn += i.Wturn_time  # 计算平均带权周转时间
    print("\r")
    print(
        "\t" * 4 + "动态高优先级优先算法 平均周转时间为:%2.2f,平均带权周转时间为:%2.2f" %
        (AV_turn / 4, AV_Wturn / 4))
    return list2


def TR(pcb_list):
    """时间片轮转法"""
    time = 0
    AV_turn = 0
    AV_Wturn = 0
    list2 = []  # 运行完毕的进程组
    remove_time = pcb_list[0].in_time - 1  # 解决就绪队列两个进程同时到达内存，却先执行后面的进程的bug

    def TR_sort(p_list):
        """每过一个时间片，将进程链重新排序"""
        ready_num = 0
        new_pcb = []
        for i in p_list:
            if time >= i.in_time:
                # i.fir = 1
                ready_num += 1
                if i.fir == 0:
                    new_pcb.append(i.pid)
        if ready_num > 1:
            # 如果上一个时间片有进程运行完毕，则进程链不做变化
            if time - 1 != remove_time:
                temp = p_list.pop(0)
                p_list.insert(ready_num - 1, temp)
            if new_pcb:
                new_pcb.clear()
        return p_list

    while pcb_list:
        print("time:", time)
        # 当前没有进程执行时，就将就绪队列按进程长度从小到大排列
        pcb_list = TR_sort(pcb_list)
        if time >= pcb_list[0].in_time:
            if pcb_list[0].fir == 0:
                print("进程" + str(pcb_list[0].pid) + "开始运行")
                pcb_list[0].start_time = time
                pcb_list[0].fir = 1
            pcb_list[0].cpu_time += 1
            pcb_list[0].remain_time -= 1
            if pcb_list[0].dy_priority:
                pcb_list[0].dy_priority -= 1
            pcb_list[0].alter_time = time
            pcb_list[0].i_output()
            if pcb_list[0].remain_time == 0:
                print("进程" + str(pcb_list[0].pid) + "运行结束")
                pcb_list[0].out_time = time + 1
                pcb_list[0].turn_time = pcb_list[0].out_time - \
                                        pcb_list[0].in_time
                pcb_list[0].Wturn_time = pcb_list[0].turn_time / \
                                         pcb_list[0].need_time
                list2.append(pcb_list[0])
                pcb_list.remove(pcb_list[0])
                remove_time = time
        time += 1
    for i in list2:
        AV_turn += i.turn_time  # 计算平均周转时间
        AV_Wturn += i.Wturn_time  # 计算平均带权周转时间
    print("\r")
    print(
        "\t" * 4 + "时间片轮转算法TR 平均周转时间为:%2.2f,平均带权周转时间为:%2.2f" %
        (AV_turn / 4, AV_Wturn / 4))
    return list2


def main(list1):
    temp_list = copy.deepcopy(list1)
    while True:
        list1 = copy.deepcopy(temp_list)
        n = input(
            "请选择算法(1、静态高优先级优先 2、动态高优先级优先 3、时间片轮转法) 4、重新录入进程:\n")
        if n == "1":
            list2 = copy.deepcopy(list1)
            sort_list(list2)
            list1 = SP(list1)
            sort_list(list1)
        elif n == "2":
            list2 = copy.deepcopy(list1)
            sort_list(list2)
            list1 = DP(list1)
            sort_list(list1)
        elif n == "3":
            list2 = copy.deepcopy(list1)
            sort_list(list2)
            list1 = TR(list1)
            sort_list(list1)
        elif n == "4":
            break
        else:
            print("输入错误，请重新输入！")


if __name__ == "__main__":
    while True:
        pcb_num = int(input("请输入进程个数(输入0退出)："))
        if pcb_num == 0:
            break
        op_type = int(input("请选择：1、随机生成   2、手工录入\n"))
        if op_type == 1:
            list1 = init(pcb_num)
            main(list1)
        elif op_type == 2:
            list1 = record_pcb(pcb_num)
            main(list1)
        else:
            print("输入错误，请重新输入！")
            input('键入回车离开')