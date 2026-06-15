import numpy as np
import matplotlib.pyplot as plt


def to_robot_frame(ord_x, ord_y, img):

    l_x = 14.7 
    ip_x = img.shape[1] 
    print(ip_x)
    l_y = 13.7  
    ip_y = img.shape[0]  
    print(ip_y)
    l_5 = 7  
    servo_to_centre = 13 

    c_x = l_x / ip_x
    c_y = l_y / ip_y

    t_r = [[0, c_y * 1.1, (l_5 / 2 - (c_y * ip_y / 2))],
            [c_x * 1.02, 0, (servo_to_centre - (c_x * ip_x / 2))]]

    points_x = []
    points_y = []

    for i in range(len(ord_x)):
        points_x.append(ord_x[i])
        points_y.append(ord_y[i])

    img_x = []
    img_y = []

    p = np.vstack((points_x, points_y, np.ones((1, len(points_x)))))


    mat = np.dot(t_r, p)

    x = mat[0]
    y = mat[1]

    plt.scatter(x, y)
    plt.show()

    return x, y


def smooth_path(x, y):

    size_x = len(x)

    short_x, short_y, smooth_x, smooth_y = [], [], [], []

    short_x.append(x[0])
    short_y.append(y[0])

    for i in range(size_x - 1):
        if (x[i + 1] == x[i] or y[i + 1] == y[i]):
            continue
        elif x[i - 1] == x[i]:
            short_x.append(x[i])
            short_y.append(y[i + 1])
        elif y[i - 1] == y[i]:
            short_x.append(x[i + 1])
            short_y.append(y[i])

    short_x.append(x[size_x - 1])
    short_y.append(y[size_x - 1])

    short_size = len(short_x)

    for i in range(short_size):
        smooth_x.append(short_x[i])
        smooth_y.append(short_y[i])
        if i < short_size - 1:
            smooth_x.append((short_x[i] + short_x[i + 1]) / 2)
            smooth_y.append((short_y[i] + short_y[i + 1]) / 2)

    final_x = smooth_x
    final_y = smooth_y

    for i in range(len(final_x)):
        print(final_x[i], final_y[i])

    return final_x, final_y


def transform_and_smooth(ord_x, ord_y, img):

    x, y = to_robot_frame(ord_x, ord_y, img)
    final_x, final_y = smooth_path(x, y)
    return final_x, final_y
