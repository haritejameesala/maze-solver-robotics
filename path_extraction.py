import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML, display
from skimage.morphology import skeletonize


def skeletonize_maze(img_erosion, img):

    ske = skeletonize(img_erosion / 255)
    plt.imshow(ske, cmap='gray')
    plt.axis("off")
    plt.show()

    points_arg = []
    for i in range(img.shape[0]): 
        for j in range(img.shape[1]): 
            if ske[i][j] == True:
                points_arg.append((j, i)) 

    return ske, points_arg


def show_grayscale_after_skeleton(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    plt.figure(figsize=(5, 5))
    plt.imshow(gray, cmap='gray')
    plt.axis("off") 
    plt.show()


def order_skeleton_points(points_arg):

    X = [p[0] for p in points_arg]
    Y = [p[1] for p in points_arg]

    min_arg = np.argmin(np.array(Y))
    ord_x = []
    ord_y = []

    x0 = X[min_arg]
    y0 = Y[min_arg]

    ord_x.append(x0)
    ord_y.append(y0)

    distance_list = []
    X.pop(0) 
    Y.pop(0) 

    for i in range(len(X)):
        min_dist = 10  
        j_min = 0  
        for j in range(len(X)):
            x1 = X[j]  
            y1 = Y[j]  

            dist = (x1 - x0) ** 2 + (y1 - y0) ** 2
            if dist < min_dist:
                min_dist = dist
                x_next = x1
                y_next = y1
                j_min = j

        ord_x.append(x_next)
        ord_y.append(y_next)


        X.pop(j_min)
        Y.pop(j_min)

        x0 = x_next
        y0 = y_next

    return ord_x, ord_y


def animate_path(img, ord_x, ord_y):

    img_copy = img.copy()
    img_copy1 = img.copy()
    num_points = len(ord_x)

    frames = []
    fig, ax = plt.subplots()
    ax.imshow(cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))  

    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_ylim(img.shape[0], 0)
    ax.set_xlim(0, img.shape[1])

    img_frame1 = img_copy1.copy()

    for i in range(num_points):
        cv2.circle(img_frame1, (ord_x[i], ord_y[i]), 2, (255, 0, 0), -1)
        img_rgb1 = cv2.cvtColor(img_frame1, cv2.COLOR_BGR2RGB)
        frames.append([ax.imshow(img_rgb1, animated=True)])

    ani = animation.ArtistAnimation(fig, frames, interval=15, blit=True, repeat_delay=1000)

    html_animation = ani.to_html5_video()
    display(HTML(html_animation))

    plt.close(fig)


def extract_path(img_erosion, img):

    ske, points_arg = skeletonize_maze(img_erosion, img)
    show_grayscale_after_skeleton(img)
    ord_x, ord_y = order_skeleton_points(points_arg)
    animate_path(img, ord_x, ord_y)
    return ord_x, ord_y