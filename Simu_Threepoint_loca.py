import matplotlib.pyplot as plt
import redundancy as redun
import thread_plot as pt
import input_dist as inp
import threading
import plot as pl


def main():

    input_df,summary_df,set = inp.input_dist()              # 输入一个空数组和原始数据 input_df,summary_df,set
    iter = redun.redundancy(input_df,summary_df,set)        # 实例化冗余迭代类对象 # plt.plot(input_df.loc[:,"X"], input_df.loc[:,"Y"], '.b')
    picture = pl.Draw()                                     # 实例化和初始化画图类对象

    for i in range(1,len(iter.input_df)):
        [X_3,Y_3,X_bar,Y_bar] = iter.calculate(i)           # 调用计算方法返回一个List
        picture.draw(X_3,Y_3,X_bar,Y_bar)                            # 画图

# add IDE git
# main 1.1
        T=1




if __name__ == '__main__':print('主仿真框架')
else:print('局部模组')
print('Simu_Threepoint_loca运行')
main()




# exitFlag = 0
#
#
# class plot_Thread(threading.Thread):  # 继承父类threading.Thread
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






# ---------------------------------------------------------------------------------- Old
# def redundancy():
#     print("redundancy run")
#     redun.redundancy()


    # redun.redundancy()



# def file_input():
# def file_output():

# def accuracy():

# def ploting（）:
# thread.start_new_thread(function, args[, kwargs] )