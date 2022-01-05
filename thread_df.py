import redundancy as redun
import plot_df as pl
import threading
import time
from queue import Queue


# exitFlag = 0
que = Queue(maxsize=0)
threadLock = threading.Lock()
threads = []  # 线程池 未使用

class data_Thread(threading.Thread):  # 继承父类threading.Thread

    def __init__(self, threadID, name, iter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.iter = iter

    def run(self):                                             # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name)
        for i in range(1, len(self.iter.input_df)):
            lists = self.iter.calculate(i)                     # 调用计算方法返回一个List
            # threadLock.acquire()
            que.put(lists)
            # threadLock.release()

            # return (X_3, Y_3, X_bar, Y_bar)
            # print("pullout", X_3, Y_3, X_bar, Y_bar)
            # savepoint()

# def savepoint():
#         picture.save(X_3, Y_3, X_bar, Y_bar)  # 存点  #此处没有引用picture，并不知道它是什么东西



class plot_Thread(threading.Thread):  # 继承父类threading.Thread
    def  __init__(self, threadID, name, figure):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.figure = figure
        # self.readque = que

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name)
        # while (not (que.empty())):
        counter=100
        while(1):
            got_que = que.get()
            print("Output_position", got_que)
            self.figure.save(got_que)
            counter -= 1
            if counter == 0:
                counter = 100
            self.figure.draw(counter)

            # figure.save(X_3, Y_3, X_bar, Y_bar)  # 存点
            # figure.draw()                                    # 画图



        # print('\n队列当前值为：', que.queue, '\n')
        # print_time(self.name, self.counter, 5)
        # print("Exiting " + self.name)



def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1










# def print_time(threadName, delay, counter):
#     while counter:
#         # if exitFlag:
#         #     (threading.Thread).exit()
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1


# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启线程
# thread1.start()
# thread2.start()
#
# print("Exiting Main Thread")



# ---------------------------------------------------------------------------------

# import threading
# import time
#
# exitFlag = 0
#
#
# class myThread(threading.Thread):  # 继承父类threading.Thread
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
#         print("Starting " + self.name)
#         print_time(self.name, self.counter, 5)
#         print("Exiting " + self.name)
#
#
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             (threading.Thread).exit()
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
#
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启线程
# thread1.start()
# thread2.start()
#
# print("Exiting Main Thread")
