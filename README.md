# Multiple_Object_Tracking

# Multi-Object Tracking using OpenCV

This project demonstrates multi-object tracking using various tracking algorithms available in OpenCV. It allows users to select multiple regions of interest (ROIs) in a video and track them using one of the available tracking algorithms. The tracker of choice in this example is CSRT, but you can easily switch between different algorithms like KCF, MIL, or MOSSE.

## Project Overview

In this project, I developed a Python script that tracks multiple objects in a video. You can manually select the objects (regions of interest - ROIs) you want to track, and the script will track them across video frames using the chosen tracking algorithm. Each object is highlighted with a bounding box, and the bounding boxes are updated in real-time as the video progresses.

## Features

- **Manual Object Selection**: Users can select one or more objects to track by drawing bounding boxes on the initial frame of the video.
- **Multi-object Tracking**: Once objects are selected, the system will track each object across subsequent frames.
- **Multiple Tracking Algorithms**: The script supports various tracking algorithms provided by OpenCV:
  - **BOOSTING**
  - **MIL**
  - **KCF**
  - **CSRT** (default)
  - **TLD**
  - **MEDIANFLOW**
  - **MOSSE**
  
- **Colored Bounding Boxes**: Each tracked object is surrounded by a bounding box of a unique color for better visualization.

## How It Works

1. **ROI Selection**: 
   - The program will pause after reading the first frame of the video, allowing the user to manually select the objects (ROIs) they want to track.
   - After selecting each object, press any key to continue selecting more objects or press 'q' to begin tracking.
   
2. **Tracking**:
   - Once all objects are selected, the chosen tracking algorithm (default is CSRT) will be used to track the objects as the video plays.
   - The bounding boxes around the objects are updated in real-time and displayed on the video window.

3. **Stopping the Program**:
   - You can stop the video and exit the program by pressing the 'q' key at any time.

## How to Run

### Dependencies

To run this project, you need to have the following libraries installed:
- `opencv-python`
- `opencv-contrib-python`

You can install these dependencies using `pip`:
```bash
pip install opencv-python opencv-contrib-python
