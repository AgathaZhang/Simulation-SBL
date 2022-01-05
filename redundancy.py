# -----------------------------------------------  冗余算法本体
import numpy as np
import numpy.random as rd
import pandas as pd
import matplotlib.pyplot as plt
import two_circle
import three_circle

# ------------------------------------------------------------------------------------- 移动至文件 input_df.py

    # input_df = pd.read_csv("F:\Project\Redundancy\Redundancy_pycode\Fix1523-1549.csv",index_col=0)
    # input_df["Time"] = [x for x in input_df.index]
    # input_df.index = range(input_df.shape[0])
    # input_df.columns = [x.strip() for x in input_df.columns]
    #
    # [a1, b1, c1] = [8.545334, 27.140783, -11.82325]  # 11-17号的基点位置
    # [a2, b2, c2] = [12.549821, 47.997643, -10.48749]
    # [a3, b3, c3] = [22.717552, 29.466097, -15.111055]
    #
    # P1 = np.array([a1, b1, c1])
    # P2 = np.array([a2, b2, c2])
    # P3 = np.array([a3, b3, c3])
    #
    # summary_df = pd.DataFrame(index=input_df.index,
    #                           columns=["X_3", "Y_3", "X_bar", "Y_bar",
    #                                    "d1", "d2", "d3", "P12_X", "P12_Y", "P13_X", "P13_Y", "P23_X", "P23_Y"])

# ------------------------------------------------------------------------------------- 移动至文件 input_df.py


class redundancy:
    def __init__(self,input_df,summary_df,set):
        print("当前为冗余算法redundancy")
        self.input_df = input_df
        self.summary_df = summary_df
        self.set = set
        self.i = []
        # return self.input_df   # 为什么不能返回dataframe


    def calculate(self,i):
        P1 = self.set[0]        # 11-17号的基点位置
        P2 = self.set[1]
        P3 = self.set[2]
        sample = i



        d1_sqr = self.input_df.loc[i, "d1"] ** 2 - (-0.5 - P1[2]) ** 2    # self.set[0][2]表示C1深度值   # 给出新的d1的平方，认为robot深度已知 0.5
        d2_sqr = self.input_df.loc[i, "d2"] ** 2 - (-0.5 - P2[2]) ** 2
        d3_sqr = self.input_df.loc[i, "d3"] ** 2 - (-0.5 - P3[2]) ** 2
        d1 = np.sqrt(d1_sqr)
        d2 = np.sqrt(d2_sqr)
        d3 = np.sqrt(d3_sqr)
        self.summary_df.loc[i, "d1"] = d1
        self.summary_df.loc[i, "d2"] = d2
        self.summary_df.loc[i, "d3"] = d3


        X_3, Y_3 = three_circle.get_three_circle_intersection_point_on_a_plane(P1, P2, P3, d1_sqr, d2_sqr, d3_sqr)
        circle_intersections_df = two_circle.get_two_circle_intersection_point_on_a_plane(P1, P2, P3, d1_sqr, d2_sqr, d3_sqr)
        circle_intersections_df["d"] = (circle_intersections_df["X"] - X_3) ** 2 + (circle_intersections_df["Y"] - Y_3) ** 2    # 计算一个与Jimmy的距离
        circle_intersections_df_top3 = circle_intersections_df.sort_values(by="d").head(3)    # 排序 sort_values
        if circle_intersections_df_top3["note_index"].unique().shape[0] == 3:  # 924-941   从6个点选出P12,P23 P13 Q 找出三个离jimmy最近的点 作为P12 P13 P23

            P12 = circle_intersections_df_top3[circle_intersections_df_top3["note_index"] == "12"][
                ["X", "Y"]].squeeze().to_list()
            P13 = circle_intersections_df_top3[circle_intersections_df_top3["note_index"] == "13"][
                ["X", "Y"]].squeeze().to_list()
            P23 = circle_intersections_df_top3[circle_intersections_df_top3["note_index"] == "23"][
                ["X", "Y"]].squeeze().to_list()
        else:
            # idx_top3_unique = circle_intersections_df_top3["note_index"].unique().tolist()
            def get_a_P(note_index, df):
                try:
                    df_selected = df[df["note_index"] == note_index][["X", "Y"]]
                    P = df_selected.squeeze().to_list()
                except AttributeError:
                    P = [None, None]
                return P


            # idx_missing = [ x for x in ["13", "12", "23"] if x not in idx_top3_unique]
            P23 = get_a_P("23", circle_intersections_df_top3)
            P13 = get_a_P("13", circle_intersections_df_top3)
            P12 = get_a_P("12", circle_intersections_df_top3)


        # ------------------------------------------------------------------------------------ 丢进一个dataframe 算平均值给结果

        output_point = pd.DataFrame(columns=["X", "Y"],data=[P12,P23,P13])  ##index=,
        # sum_pointadd = pd.DataFrame(columns=["X", "Y"])
        # sum_pointadd = [0,0]
        sum_X = 0;sum_Y = 0;zero = 0
        for temp in output_point.index:
            # sum_pointadd = sum_pointadd + output_point.loc[temp,"X"]
            if np.isnan(output_point.loc[temp, "X"]):
                zero = zero+1
                continue
            else:
                sum_X= sum_X + output_point.loc[temp, "X"]
                sum_Y= sum_Y + output_point.loc[temp, "Y"]
        try:
            X_bar = sum_X / (3 - zero)
            Y_bar = sum_Y / (3 - zero)
        except ZeroDivisionError:
            X_bar = 0
            Y_bar = 0
            # X_bar = None
            # Y_bar = None
            # list wujie 待调研
            # 三个都不存在的情况 待coding

        #     # sum_pointadd = sum_pointadd+output_point.loc[temp, "X"]
        #     # sum_pointadd = sum_pointadd + output_point.loc[temp]
        #     sum_pointadd = sum_pointadd + output_point[temp]
        # pd.DataFrame[i] = pd.Series(index)
        #.unique().shape[0] == 3
        if abs(X_3) > 200:X_3 = 0
        if abs(Y_3) > 200: Y_3 = 0
        if abs(X_bar) > 200: X_bar = 0
        if abs(Y_bar) > 200: Y_bar = 0
        lists = [X_3, Y_3, X_bar, Y_bar]

        return lists  # 循环应该放在reduncy那一层，这里只返回每一次的





# # ----------------------------------------------------------------------------------------------------------
# #         X_bar = None if P12[0] is None or P13[0] is None or P23[0] is None\
# #                 else (P12[0] + P13[0] + P23[0]) / 3.0  # 找出三个点求平均 None if 和  is None or 复习
# #
# #         Y_bar = None if P12[1] is None or P13[1] is None or P23[1] is None\
# #                 else (P12[1] + P13[1] + P23[1]) / 3.0
# # -----------------------------------------------------------------------------------------------------------
#         summary_df.loc[i, "X_3"] = X_3  # 存储
#         summary_df.loc[i, "Y_3"] = Y_3
#         summary_df.loc[i, "X_bar"] = X_bar
#         summary_df.loc[i, "Y_bar"] = Y_bar
#         summary_df.loc[i, "P12_X"] = P12[0]
#         summary_df.loc[i, "P12_Y"] = P12[1]
#         summary_df.loc[i, "P13_X"] = P13[0]
#         summary_df.loc[i, "P13_Y"] = P13[1]
#         summary_df.loc[i, "P23_X"] = P23[0]
#         summary_df.loc[i, "P23_Y"] = P23[1]
#
#     # summary_df.index = input_df["Time"]
#     # summary_df.to_csv("F:\Project\Redundancy\Redundancy_pycode\Result.csv")
#     return X_3,Y_3,X_bar,Y_bar
#
#
# redundancy()


