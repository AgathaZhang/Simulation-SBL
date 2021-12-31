# import pandas as pd
# import numpy as np
#
# [a1, b1, c1] = [8.545334, 27.140783, -11.82325]
# P1 = np.array([a1, b1, c1])
# z=P1[3]
# t=1


import matplotlib.pyplot as plt
import numpy as np
import time
from math import *
#
# plt.ion() #开启interactive mode 成功的关键函数
# plt.figure(1)
# t = [0]
# t_now = 0
# m = [sin(t_now)]
#
# for i in range(2000):
# 	plt.clf() #清空画布上的所有内容
# 	t_now = i*0.1
# 	t.append(t_now)#模拟数据增量流入，保存历史数据
# 	m.append(sin(t_now))#模拟数据增量流入，保存历史数据
# 	plt.plot(t,m,'-r')
# 	plt.pause(0.01)
# import builtins
# class JustCounter:
# 	__secretCount = 0  # 私有变量
# 	publicCount = 0  # 公开变量
#
# 	def count(self):
# 		self.__secretCount += 1
# 		self.publicCount += 1
# 		print(self.__secretCount)
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
#
# dir(builtins)
import pandas as pd
import numpy as np
# data = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)],
#                 dtype=[("a"), ("b"), ("c")])
# df3 = pd.DataFrame(data, columns=['c', 'a'])
# t=1   A = file_output_filter(i)
# print dir(t)

# ------------------------------------------------------------------------------------ 丢进一个dataframe 算平均值给结果
#
# output_point = pd.DataFrame(columns=["X", "Y"], data=[P12, P23, P13])  ##index=,
# # sum_pointadd = pd.DataFrame(columns=["X", "Y"])
# # sum_pointadd = [0,0]
# sum_X = 0
# sum_Y = 0
# howmuch_none = 0
# for temp in output_point.index:
#     # sum_pointadd = sum_pointadd + output_point.loc[temp,"X"]
#     if np.isnan(output_point.loc[temp, "X"]):
#         howmuch_none = howmuch_none + 1
#         continue
#     else:
#         sum_X = sum_X + output_point.loc[temp, "X"]
#         sum_Y = sum_Y + output_point.loc[temp, "Y"]
#
# X_bar = sum_X / (3 - howmuch_none)
# Y_bar = sum_Y / (3 - howmuch_none)
# ------------------------------------------------------------------------------------

# ----------------------------------------------------------------------
#         plt.clf()  # 清空画布上的所有内容
#         # t_now = X_bar
#         t.append(X_bar)  # 模拟数据增量流入，保存历史数据
#         m.append(Y_bar)  # 模拟数据增量流入，保存历史数据
#         plt.plot(t, m, '.b')
#         plt.show()
#         # plt.pause(0.01)
# ----------------------------------------------------------------------
# x = "a"
# y = "b"
# # 换行输出
# print(x)
# print(y)
#
# print('---------')
# # 不换行输出
# print(x)
# print(y, end=" ")
# print()
#
# list1 = []
# list2 = ("15",)
# tupl = 'd'
# t=1;

# dict = {}
# dict['one'] = "1 - 菜鸟教程"
# dict[2]     = "2 - 菜鸟工具"
#
# tuple1 = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
# a=tuple(fes,[3])
# tinydict = {tuple('queue'): 'runoob','code':'Fred', 'site': 'www.runoob.com'}
#
#
# print (dict['one'])       # 输出键为 'one' 的值
# print (dict[2])           # 输出键为 2 的值
# print (tinydict)          # 输出完整的字典
# print (tinydict.keys())   # 输出所有键
# print (tinydict.values()) # 输出所有值
# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
#
# # 实例化类
# # p = people('runoob', 10, 30)
# people.speak(1)
# pp=1;

# import sys
#
# sum=5
# def add(a=1,b=3):
#     print (a,b)
#     print (sum)   #仅仅访问
# add(4,8)
# print (sum)

# ---------------------------------------------
# import sys
# sum=5
# def add(a=1,b=3):
#     print (a,b)
#     print (sum)                                                 #内部函数引用同名变量，并且修改这个变量。python会认为它是局部变量。因为在此处print之前，没有定义sum变量，所以会报错（建议与情况一比较，备注：此处只是比上例先print sum）
#     # sum=b+a
#     # print (sum)
# add(4,8)
# print (sum)

# import pandas as pd
#
# sites = {1: "Google", 'Key': "Runoob", 3: "Wiki"}
#
# A = pd.Series(sites)
#
# print(A)
# print(A)

# var = "foo"
# tt=dir(var)
# print (dir(var))

# ----------------------------------------------------- 引用变量的名字
# import inspect
#
# def retrieve_name(var):
#     callers_local_vars = inspect.currentframe().f_back.f_locals.items()
#     return [var_name for var_name, var_val in callers_local_vars if var_val is var]
#
# name, address, age, gender = "bob", "hangzhou", 21, "man"
# person = {}
#
# for i in [name, address, age, gender]:
#     person[retrieve_name(i)[0]] = i
#
# print (person)
#
# t=1
# --------------------------------------------------------- 多线程
# import threading
# import time
#
#
# # 为线程定义一个函数
# def print_time(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print
#         "%s: %s" % (threadName, time.ctime(time.time()))
#
#
# # 创建两个线程
# try:
#     thread.start_new_thread(print_time, ("Thread-1", 2,))
#     thread.start_new_thread(print_time, ("Thread-2", 4,))
# except:
#     print
#     "Error: unable to start thread"
#
# while 1:
#     print
#     "Error: unable to start thread"
# -------------------------------------------------------------------------------------
import threading
import time

exitFlag = 0


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)



def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

print("Exiting Main Thread")

t = 1





# T=1