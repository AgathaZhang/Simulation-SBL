import numpy as np
import numpy.random as rd
import pandas as pd
import matplotlib.pyplot as plt



def input_dist():    # def input
    input_df = pd.read_csv("F:\Project\Redundancy\Redundancy_pycode\Fix1523-1549.csv", index_col=0)
    input_df["Time"] = [x for x in input_df.index]
    input_df.index = range(input_df.shape[0])
    input_df.columns = [x.strip() for x in input_df.columns]

    [a1, b1, c1] = [8.545334, 27.140783, -11.82325]  # 11-17号的基点位置
    [a2, b2, c2] = [12.549821, 47.997643, -10.48749]
    [a3, b3, c3] = [22.717552, 29.466097, -15.111055]

    P1 = np.array([a1, b1, c1])
    P2 = np.array([a2, b2, c2])
    P3 = np.array([a3, b3, c3])
    set = [P1,P2,P3]

    summary_df = pd.DataFrame(index=input_df.index,
                              columns=["X_3", "Y_3", "X_bar", "Y_bar",
                                       "d1", "d2", "d3", "P12_X", "P12_Y", "P13_X", "P13_Y", "P23_X", "P23_Y"])
    return [input_df,summary_df,set]




# The following is the test content
# A = input_dist()
# t=1