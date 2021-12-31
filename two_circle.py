import numpy as np
import numpy.random as rd
import pandas as pd
import matplotlib.pyplot as plt


def get_two_circle_intersection_point_on_a_plane(P1, P2, P3, d1_sqr, d2_sqr, d3_sqr):  # 解方程
    [a1, b1] = P1[0],P1[1]
    [a2, b2] = P2[0],P2[1]
    [a3, b3] = P3[0],P3[1]

    const12 = -1 * (d1_sqr - a1 ** 2 - b1 ** 2 - d2_sqr + a2 ** 2 + b2 ** 2) / 2.0
    const23 = -1 * (d2_sqr - a2 ** 2 - b2 ** 2 - d3_sqr + a3 ** 2 + b3 ** 2) / 2.0
    const13 = -1 * (d1_sqr - a1 ** 2 - b1 ** 2 - d3_sqr + a3 ** 2 + b3 ** 2) / 2.0

    #### get two intersection points with 2 circles
    ### (a1-a2) * x + (b1 - b2) * y = -1 *(d1_sqr -c1**2 - a1**2 -b1**2 - d2_sqr +c2**2 + a2**2 + b2**2) / 2.0
    ### eq1 - eq2: x  = const12/ (a1-a2) - (b1 - b2)/(a1-a2) * y, alpha=const12/ (a1-a2), beta= -(b1 - b2)/(a1-a2)
    ### eq2 - eq1: y  = const12/ (b1-b2) - (a1 - a2)/(b1-b2) * y, alpha=const12/ (b1-b2), beta= -(a1 - a2)/(b1-b2)
    alpha = const12 / (a1 - a2)
    beta = -(b1 - b2) / (a1 - a2)
    a = (beta ** 2 + 1)
    b = (2 * beta * (alpha - a1) - 2 * b1)  # b = (2 * beta * (a1 - alpha ) - 2 * b1)
    c = (alpha - a1) ** 2 + b1 ** 2 - d1_sqr
    D = b ** 2 - 4 * a * c
    Y12_pos = (-1 * b + np.sqrt(D)) / (2.0 * a)               # 先求了y
    Y12_neg = (-1 * b - np.sqrt(D)) / (2.0 * a)
    X12_pos = const12 / (a1 - a2) - (b1 - b2) / (a1 - a2) * Y12_pos
    X12_neg = const12 / (a1 - a2) - (b1 - b2) / (a1 - a2) * Y12_neg
    # logger.info("eq1 - eq2: ({x1}, {y1}), ({x2}, {y2})".format(x1=X12_pos, y1=Y12_pos, x2=X12_neg, y2=Y12_neg))  # 一元二次方程
# ---------------------------------------------------------------------------------------------------
#     alpha = const12 / (b1 - b2)
#     beta = -(a1 - a2) / (b1 - b2)
#     a = (beta ** 2 + 1)
#     b = (2 * beta * (alpha - b1) - 2 * a1)  # b = (2 * beta * (a1 - alpha ) - 2 * b1)
#     c = (b1 - alpha) ** 2 + a1 ** 2 - d1_sqr
#     D = b ** 2 - 4 * a * c
#     x12_pos = (-1 * b + np.sqrt(D)) / (2.0 * a)               # 先求了x
#     x12_neg = (-1 * b - np.sqrt(D)) / (2.0 * a)
#     y12_pos = const12 / (b1 - b2) - (a1 - a2) / (b1 - b2) * Y12_pos
#     y12_neg = const12 / (b1 - b2) - (a1 - a2) / (b1 - b2) * Y12_neg
# ---------------------------------------------------------------------------------------------------

    #### eq2 - eq3： x = const23/(a2-a3) - (b2 - b3)/(a2-a3) * y,
    ###eq2 - eq3:  y = const23/(b2 - b3) - (a2-a3)/(b2 - b3) * x
    alpha = const23 / (a2 - a3)
    beta = -(b2 - b3) / (a2 - a3)
    a = (beta ** 2 + 1)
    b = (2 * beta * (alpha - a2) - 2 * b2)
    c = (alpha - a2) ** 2 + b2 ** 2 - d2_sqr
    D = b ** 2 - 4 * a * c
    Y23_pos = (-1 * b + np.sqrt(D)) / (2.0 * a)
    Y23_neg = (-1 * b - np.sqrt(D)) / (2.0 * a)
    X23_pos = const23 / (a2 - a3) - (b2 - b3) / (a2 - a3) * Y23_pos
    X23_neg = const23 / (a2 - a3) - (b2 - b3) / (a2 - a3) * Y23_neg
    # logger.info("eq2 - eq3: ({x1}, {y1}), ({x2}, {y2})".format(x1=X23_pos, y1=Y23_pos, x2=X23_neg, y2=Y23_neg))

    ####eq1 - eq3: x  = const13/(a1-a3) - (b1 - b3)/(a1-a3) * y
    ###eq1 - eq3:  y = const13/(b1 - b3) - (a1-a3)/(b1 - b3) * x
    ###eq1 - eq3:  y = const13/(b1 - b3) - (a1-a3)/(b1 - b3) * x
    ### calc X first
    # alpha = const13/(b1 - b3)
    # beta = - (a1-a3)/(b1 - b3)
    # a = (beta**2 + 1)
    # b = (2*beta*(alpha - b1) - 2*a1)
    # c = (alpha - b1)**2 + a1**2 - d1_sqr + c1**2
    # D = b**2 - 4*a*c
    # X13_pos = (-1 *b + np.sqrt(D))/(2.0 * a)
    # X13_neg = (-1 *b - np.sqrt(D))/(2.0 * a)
    # Y13_pos = const13/(b1 - b3) - (a1-a3)/(b1 - b3) * X13_pos
    # Y13_neg = const13/(b1 - b3) - (a1-a3)/(b1 - b3) * X13_neg
    # logger.info("eq1 - eq3: ({x1}, {y1}), ({x2}, {y2})".format(x1=X13_pos, y1=Y13_pos, x2=X13_neg, y2=Y13_neg))
    ##############################
    alpha = const13 / (a1 - a3)
    beta = -(b1 - b3) / (a1 - a3)
    a = (beta ** 2 + 1)
    b = (2 * beta * (alpha - a1) - 2 * b1)
    c = (alpha - a1) ** 2 + b1 ** 2 - d1_sqr
    D = b ** 2 - 4 * a * c
    Y13_pos = (-1 * b + np.sqrt(D)) / (2.0 * a)
    Y13_neg = (-1 * b - np.sqrt(D)) / (2.0 * a)
    X13_pos = const13 / (a1 - a3) - (b1 - b3) / (a1 - a3) * Y13_pos
    X13_neg = const13 / (a1 - a3) - (b1 - b3) / (a1 - a3) * Y13_neg
    # logger.info("eq1 - eq3: ({x1}, {y1}), ({x2}, {y2})".format(x1=X13_pos, y1=Y13_pos, x2=X13_neg, y2=Y13_neg))  # 指示的哪个点

    circle_intersections_df = pd.DataFrame(index=range(6), columns=["X", "Y", "note_index", "note_sign"])
    circle_intersections_df.loc[0, "X"] = X12_pos
    circle_intersections_df.loc[0, "Y"] = Y12_pos
    circle_intersections_df.loc[0, "note_index"] = "12"
    circle_intersections_df.loc[0, "note_sign"] = "pos"
    circle_intersections_df.loc[1, "X"] = X12_neg
    circle_intersections_df.loc[1, "Y"] = Y12_neg
    circle_intersections_df.loc[1, "note_index"] = "12"
    circle_intersections_df.loc[1, "note_sign"] = "neg"
    circle_intersections_df.loc[2, "X"] = X23_pos
    circle_intersections_df.loc[2, "Y"] = Y23_pos
    circle_intersections_df.loc[2, "note_index"] = "23"
    circle_intersections_df.loc[2, "note_sign"] = "pos"
    circle_intersections_df.loc[3, "X"] = X23_neg
    circle_intersections_df.loc[3, "Y"] = Y23_neg
    circle_intersections_df.loc[3, "note_index"] = "23"
    circle_intersections_df.loc[3, "note_sign"] = "neg"
    circle_intersections_df.loc[4, "X"] = X13_pos
    circle_intersections_df.loc[4, "Y"] = Y13_pos
    circle_intersections_df.loc[4, "note_index"] = "13"
    circle_intersections_df.loc[4, "note_sign"] = "pos"
    circle_intersections_df.loc[5, "X"] = X13_neg
    circle_intersections_df.loc[5, "Y"] = Y13_neg
    circle_intersections_df.loc[5, "note_index"] = "13"
    circle_intersections_df.loc[5, "note_sign"] = "neg"
    # circle_intersections_df.to_csv("F:\\robot\\example.csv")
    return circle_intersections_df