from preprocessing import preprocess
from path_extraction import extract_path
from smoothing import transform_and_smooth
from inverse_kinematics import run_inverse_kinematics


def main():
    filename = 'genesis_26'

    # 1. Preprocessing 
    img, img_erosion = preprocess('genesis_maze.png')

    # 2. Path Extraction 
    ord_x, ord_y = extract_path(img_erosion, img)

    # 3. Coordinate Transform + Smoothing 
    final_x, final_y = transform_and_smooth(ord_x, ord_y, img)

    # 4. Inverse Kinematics + Export 
    theta_1_new, theta_4_new = run_inverse_kinematics(final_x, final_y, csv_filename='Angles.csv')


if __name__ == '__main__':
    main()
