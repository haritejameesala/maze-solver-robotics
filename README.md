# Maze Solver using Computer Vision and Robotic Inverse Kinematics

This project was developed as part of the **Genesis Workshop conducted by RMI (Robotics and Machine Intelligence), NIT Trichy**.

The system takes a maze image as input, extracts the valid path using computer vision techniques, transforms the path into the robot’s coordinate frame, smooths it, and computes joint angles for robotic execution using inverse kinematics.

---

## Project Overview

The objective is to automate maze path extraction and convert it into executable robotic motion.

Pipeline:

```text
Maze Image
   ↓
Preprocessing
   ↓
Skeletonization
   ↓
Path Ordering
   ↓
Coordinate Transformation
   ↓
Path Smoothing
   ↓
Inverse Kinematics
   ↓
Servo Angles (CSV)
```

---

## Features

- Maze preprocessing using OpenCV
- Contour extraction and cleaning
- Skeletonization for path thinning
- Nearest-neighbor path ordering
- Coordinate transformation from image space → robot space
- Path smoothing for better robotic movement
- Inverse kinematics for dual-arm robotic control
- CSV export of servo angles

---

## Tech Stack

- **Python**
- **OpenCV**
- **NumPy**
- **Matplotlib**
- **Pandas**
- **scikit-image**

---

## Project Structure

```text
maze_solver/
│── preprocessing.py        # Image preprocessing pipeline
│── path_extraction.py      # Skeleton extraction and path ordering
│── smoothing.py            # Coordinate transform and smoothing
│── inverse_kinematics.py   # Joint angle computation
│── main.py                 # Main execution file
│── requirements.txt
│── README.md
│── genesis_maze.png        # Input maze image
│── Angles.csv              # Output servo angles
```

---

## Methodology

### 1. Preprocessing

The maze image undergoes:

- RGB → Grayscale conversion
- Binary inversion thresholding
- Contour detection
- Outer boundary removal
- Morphological dilation and erosion
- Difference extraction

Purpose:

To isolate the valid maze path while removing noise.

---

### 2. Skeletonization

The cleaned path is skeletonized into a one-pixel-wide path.

Purpose:

To preserve topology while simplifying traversal.

---

### 3. Path Ordering

All skeleton points are ordered using nearest-neighbor traversal.

Purpose:

To reconstruct the actual path sequence.

---

### 4. Coordinate Transformation

Pixel coordinates are transformed into the robot’s physical workspace using an affine transform.

Purpose:

To convert image-space into real-world robot coordinates.

---

### 5. Path Smoothing

Corner-shortcutting and midpoint interpolation are used.

Purpose:

To reduce abrupt robotic movement.

---

### 6. Inverse Kinematics

The smoothed path is converted into:

- **Theta 1**
- **Theta 4**

for the robotic arm.

Output is stored in:

```text
Angles.csv
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/haritejameesala/maze-solver-robotics.git
cd maze_solver
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python main.py
```

---

## Input

Place your maze image inside the project folder:

```text
genesis_maze.png
```

---

## Output

### Processed Pipeline

- Thresholded maze
- Clean contour
- Skeletonized path
- Ordered traversal

### Robot Output

```text
Angles.csv
```

Contains:

| THETA 1 | THETA 4 |
|---------|---------|

Used for robotic execution.

---

## Learning Outcomes

This project demonstrates:

- Image processing pipelines
- Computational geometry
- Path planning
- Robot kinematics
- Coordinate system transformations

---

## Acknowledgements

Special thanks to:

**RMI (Robotics and Machine Intelligence), NIT Trichy**  
for conducting the **Genesis Workshop** and providing the learning foundation for this project.

---

## Future Improvements

- Real-time camera input
- Better path optimization
- Obstacle-aware planning
- Physical robot integration
- ROS integration

---
