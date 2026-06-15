import cv2
import numpy as np
import matplotlib.pyplot as plt


def load_image(image_path):

    img = cv2.imread(image_path) 
    if img is None:
        print("Error: Image not found. Check filename or upload the file.")
        return None
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def to_grayscale(img, show_axis="on"):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  

    return gray


def invert_and_threshold(gray):

    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    return thresh


def find_and_draw_contours(thresh, img):

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    print(len(contours))

    width = img.shape[1]
    height = img.shape[0]
    example1 = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
    example2 = cv2.drawContours(example1, contours, 0, (255, 0, 0), 2)
    example3 = cv2.drawContours(example2, contours, 1, (0, 255, 0), 2)


    temp1 = np.copy(thresh)
    contours1 = cv2.drawContours(temp1, contours, 0, (255, 255, 255), 5)

    return contours, contours1


def hide_outer_contour(contours1, contours):

    final_contour = cv2.drawContours(contours1, contours, 1, (0, 0, 0), 5)

    return final_contour


def remove_noise(final_contour):

    ret, thresh = cv2.threshold(final_contour, 240, 255, cv2.THRESH_BINARY)

    return thresh


def dilate_and_erode(thresh):

    ke = 19
    kernel = np.ones((ke, ke), np.uint8)

    dilation = cv2.dilate(thresh, kernel, iterations=2)

    erosion = cv2.erode(dilation, kernel, iterations=1)

    return dilation, erosion


def compute_difference(dilation, erosion):
 
    diff = cv2.absdiff(dilation, erosion)

    kernel1 = np.ones((5, 5), np.uint8)
    img_erosion = cv2.erode(diff, kernel1, iterations=1)

    return img_erosion


def preprocess(image_path):
    img = load_image(image_path)
    if img is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    gray = to_grayscale(img, show_axis="off")
    thresh = invert_and_threshold(gray)
    contours, contours1 = find_and_draw_contours(thresh, img)
    final_contour = hide_outer_contour(contours1, contours)
    thresh2 = remove_noise(final_contour)
    dilation, erosion = dilate_and_erode(thresh2)
    img_erosion = compute_difference(dilation, erosion)

    images = [
        ("Original", img),
        ("Gray", gray),
        ("Threshold", thresh),
        ("Contours", contours1),
        ("Final Contour", final_contour),
        ("Cleaned", thresh2),
        ("Dilated", dilation),
        ("Final Path", img_erosion)
    ]

    fig, axs = plt.subplots(2, 4, figsize=(22, 12))

    for ax, (title, im) in zip(axs.flatten(), images):
        if len(im.shape) == 2:
            ax.imshow(im, cmap="gray")
        else:
            ax.imshow(im)

        ax.set_title(title, fontsize=14)
        ax.axis("off")

    plt.tight_layout()
    plt.show()

    return img, img_erosion