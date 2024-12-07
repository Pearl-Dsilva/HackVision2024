# HackVision2024
### Computer Vision Final Project to create a Traffic Congestion Detection system using YOLO V8.

This repository contains a Python-based vehicle tracking and counting system using YOLOv8, OpenCV, and geometric analysis to track and count vehicles in a traffic video. It employs the following key components:

### Libraries and Dependencies:
- **OpenCV** for image processing and video handling.
- **Ultralytics YOLO** for object detection and vehicle classification.
- **Shapely** for geometric operations, used to define and check if vehicles are inside defined polygon areas.
- **CVZone** for adding annotations to the frames.

### Key Features:
- **Tracker Class**: A custom class to track detected objects by maintaining their center points and assigning unique IDs.
- **Vehicle Detection**: The YOLOv8 model is used to detect vehicles such as cars, buses, and trucks.
- **Vehicle Counting**: The system tracks vehicles entering and exiting two defined polygonal zones in the video, counting cars, buses, and trucks separately for each zone.
- **Geometric Operations**: The system checks if a vehicle's center point lies inside predefined polygons, indicating whether the vehicle has crossed the area.
- **Output**: The video output is annotated with vehicle counts and ID tags, and the processed video is saved with these annotations.

### Workflow:
1. Load the video file and YOLO model.
2. Process each frame of the video, detecting vehicles and tracking their movements.
3. Count vehicles based on their position relative to two polygons.
4. Annotate the frames with vehicle IDs, counts, and polygon boundaries.
5. Save the output video and print the total vehicle count for each type.

### Use Case:
This system is designed to analyze traffic videos for congestion monitoring or traffic flow analysis, counting the number of cars, buses, and trucks passing through two zones in real-time.

### Requirements:
- **Python libraries**: `torch`, `ultralytics`, `cvzone`, `shapely`, `opencv-python`, `numpy`, `pandas`.
- **YOLOv8 model**: Pre-trained model is required for detection.

This project demonstrates an efficient use of deep learning for real-time vehicle tracking and traffic analysis.

### Video:
<a href="http://www.youtube.com/watch?feature=player_embedded&v=ChudKmGyOfA
" target="_blank"><img src="http://img.youtube.com/vi/ChudKmGyOfA/0.jpg" 
alt="Traffic Congestion Detection system using YOLO V8" width="240" height="180" border="10" /></a>

