# Hand Gesture Brightness Control

This project uses computer vision and hand tracking to control screen brightness through hand gestures. It utilizes OpenCV, MediaPipe, and screen-brightness-control libraries to detect hand movements and adjust the screen brightness accordingly.
![zoom-fingers](https://github.com/user-attachments/assets/1c10dc50-38b8-49ef-b1bc-5e3c2acf2731)

## Features

- Real-time hand tracking using webcam
- Screen brightness control using thumb and index finger distance
- Visual feedback with hand landmark drawing

## Requirements

- Python 3.6+
- OpenCV
- MediaPipe
- screen-brightness-control

## Installation

1. Clone this repository or download the script.

2. Install the required libraries:

## Usage

1. Run the script:


2. Position your hand in front of the webcam.

3. Move your thumb and index finger closer together or farther apart to adjust the screen brightness.

4. Press 'q' to quit the application.

## How it works

The script captures video from the webcam and uses MediaPipe to detect and track hand landmarks. It calculates the distance between the thumb tip and index finger tip. Changes in this distance are used to adjust the screen brightness.

## Customization

You can adjust the `brightness_change_threshold` variable in the script to make the brightness control more or less sensitive to hand movements.


## Acknowledgments

- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- [screen-brightness-control](https://github.com/Crozzers/screen_brightness_control)
