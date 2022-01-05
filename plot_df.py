# -----------------------------------------------  定义一个画图类
import matplotlib.pyplot as plt


class Draw:
    # __i = 5

    def __init__(self):
        self.X_re = []
        self.Y_re = []
        self.X_bar = []
        self.Y_bar = []

    def save(self, got_que):
        plt.clf()                            # 清空画布上的所有内容
        self.X_re.append(got_que[0])   # X               # 模拟数据增量流入，保存历史数据
        self.Y_re.append(got_que[1])            # Y       # 模拟数据增量流入，保存历史数据
        self.X_bar.append(got_que[2])        # X_bar
        self.Y_bar.append(got_que[3])        # Y_bar

    def draw(self, counter):
        if counter == 1:
            plt.plot(self.X_re, self.Y_re, '.b')
            plt.plot(self.X_bar, self.Y_bar, '.r')
            # plt.plot
            plt.show()

    # def draw2(self, X_bar, Y_bar):
    #     # plt.clf()                                # 清空画布上的所有内容
    #     self.X_re.append(X_bar)                  # 模拟数据增量流入，保存历史数据
    #     self.Y_re.append(Y_bar)                  # 模拟数据增量流入，保存历史数据
    #     plt.plot(self.X_re, self.Y_re, '.r')
    #     plt.show()
# ---------------------------------------------------------------- 待处理
# class Draw:
#
#     def draw(self,X,Y,X_bar, Y_bar):
#
#         plt.plot(X,Y,'.b')
#         plt.plot(X_bar,Y_bar,'.r')
#         plt.show()


# ---------------------------------------------------------------- 待处理
#         global __i
#         __i = __i - 1
#
#         if __i == 1:  # 每5个新点画一幅图
#             __i = 5
#             plt.plot(self.X_re, self.Y_re, '.b')
#             plt.show()
#             # plt.pause(0.01)