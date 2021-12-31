import numpy as np
import numpy.random as rd
import pandas as pd
import matplotlib.pyplot as plt

def get_three_circle_intersection_point_on_a_plane(P1, P2, P3, d1_sqr, d2_sqr, d3_sqr):
    [a1, b1] = P1[0],P1[1]
    [a2, b2] = P2[0],P2[1]
    [a3, b3] = P3[0],P3[1]

    const12 = -1 * (d1_sqr - a1 ** 2 - b1 ** 2 - d2_sqr + a2 ** 2 + b2 ** 2) / 2.0
    const23 = -1 * (d2_sqr - a2 ** 2 - b2 ** 2 - d3_sqr + a3 ** 2 + b3 ** 2) / 2.0
    const13 = -1 * (d1_sqr - a1 ** 2 - b1 ** 2 - d3_sqr + a3 ** 2 + b3 ** 2) / 2.0

    # first point
    A12_23 = np.array([[(a1 - a2), (b1 - b2)],
                       [(a2 - a3), (b2 - b3)]])
    A12_23_inv = np.linalg.inv(A12_23)
    b12_23 = np.array([[const12],
                       [const23]])
    X12_23, Y12_23 = np.dot(A12_23_inv, b12_23).squeeze()   # 待学
    # logger.info("first point: X={x}, Y={y}".format(x=X12_23, y=Y12_23))    # 待学

    #### second point
    A23_13 = np.array([[(a2 - a3), (b2 - b3)],
                       [(a1 - a3), (b1 - b3)]])
    A23_13_inv = np.linalg.inv(A23_13)
    b23_13 = np.array([[const23],
                       [const13]])
    X12_13, Y12_13 = np.dot(A23_13_inv, b23_13).squeeze()
    # logger.info("second point: X={x}, Y={y}".format(x=X12_13, y=Y12_13))

    #### third point
    A12_13 = np.array([[(a1 - a2), (b1 - b2)],
                       [(a1 - a3), (b1 - b3)]])
    A12_13_inv = np.linalg.inv(A12_13)
    b12_13 = np.array([[const12],
                       [const13]])
    X12_13, Y12_13 = np.dot(A12_13_inv, b12_13).squeeze()             #  其中一种情况可能无解
    # logger.info("third point: X={x}, Y={y}".format(x=X12_13, y=Y12_13))

    return X12_13, Y12_13