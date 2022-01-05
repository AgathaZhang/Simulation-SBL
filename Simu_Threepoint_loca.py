import matplotlib.pyplot as plt
import redundancy as redun
import thread_df as th
import input_df as inp
import plot_df as pl
import threading
# import time

def main():
    input_df, summary_df, set = inp.input_dist()              # 输入一个空数组和原始数据 input_df,summary_df,set
    iter = redun.redundancy(input_df, summary_df, set)        # 实例化冗余迭代类对象 # plt.plot(input_df.loc[:,"X"], input_df.loc[:,"Y"], '.b')
    figure = pl.Draw()                                        # 实例化和初始化画图类对象

    thread1 = th.data_Thread(1, "Data_thread", iter)
    thread2 = th.plot_Thread(2, "Plot_thread", figure)

    thread1.start()   # 在线程1之后 print(q)看看有没有传进线程2
    thread2.start()
    threading.activeCount()


    # # 添加线程到线程列表
    # threads.append(thread1)
    # threads.append(thread2)
    #
    # # 等待所有线程完成
    # for t in threads:
    #     t.join()
    # print("Exiting Main Thread")

    # for i in range(1, len(iter.input_df)):
    #
    #
    #     # [X_3,Y_3,X_bar,Y_bar] = iter.calculate(i)           # 调用计算方法返回一个List
    #     figure.save(X_3,Y_3,X_bar,Y_bar)                 # 存点
    #     figure.draw()                                    # 画图
    #
    print("Stop")




if __name__ == '__main__':print('主仿真框架')
else:print('局部模组')
print('Simu_Threepoint_loca运行')
# exitFlag = 0
main()











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