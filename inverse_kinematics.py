import math
import pandas as pd


def compute_inverse_kinematics(final_x, final_y):

    la = 14  
    lb = 20  
    lc = 6.7  
    N_Points = len(final_x)

    theta_1 = []
    theta_4 = []
    for i in range(0, N_Points):
        xp = final_x[i]
        yp = final_y[i]

        E1 = -2 * la * xp
        E4 = 2 * la * (-xp + lc)

        F1 = -2 * la * yp
        F4 = -2 * la * yp

        G1 = la ** 2 - lb ** 2 + xp ** 2 + yp ** 2
        G4 = lc ** 2 + la ** 2 - lb ** 2 + xp ** 2 + yp ** 2 - 2 * lc * xp

        temp1 = math.sqrt(E1 ** 2 + F1 ** 2 - G1 ** 2)
        temp4 = math.sqrt(E4 ** 2 + F4 ** 2 - G4 ** 2)

        m1 = G1 - E1
        m4 = G4 - E4

        theta1_pos = 2 * math.atan((-F1 + temp1) / m1)
        theta1_neg = 2 * math.atan((-F1 - temp1) / m1)

        theta4_pos = 2 * math.atan((-F4 + temp4) / m4)
        theta4_neg = 2 * math.atan((-F4 - temp4) / m4)

        theta1_pos = math.degrees(theta1_pos)
        theta1_neg = math.degrees(theta1_neg)
        theta4_pos = math.degrees(theta4_pos)
        theta4_neg = math.degrees(theta4_neg)

        theta_1.append(theta1_pos)
        theta_4.append(theta4_neg)

    theta_1_new = []
    theta_4_new = []

    for i in range(0, N_Points):
        if theta_1[i] < 0:
            temp = 1 * (theta_1[i] + 270)

        if theta_1[i] > 0:
            temp = theta_1[i] - 90

        theta_1_new.append(temp)
        theta_4_new.append(theta_4[i] + 90)

    return theta_1_new, theta_4_new


def save_angles_csv(theta_1_new, theta_4_new, csv_filename='Angles.csv'):

    data = {'THETA 1': theta_1_new, 'THETA 4': theta_4_new}

    df = pd.DataFrame(data)

    df.to_csv(csv_filename, index=False)

    print(f"Successfully downloaded {csv_filename}")


def run_inverse_kinematics(final_x, final_y, csv_filename='Angles.csv'):

    theta_1_new, theta_4_new = compute_inverse_kinematics(final_x, final_y)
    save_angles_csv(theta_1_new, theta_4_new, csv_filename)
    return theta_1_new, theta_4_new
