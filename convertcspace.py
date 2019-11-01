import cv2
import numpy as np

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not camera.isOpened():
    raise IOError("Cannot open webcam")

while 1:
    # Take each frame
    _, frame = camera.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90, 1, 1])
    upper_blue = np.array([150, 255, 255])

    lower_green = np.array([30, 0, 0])
    upper_green = np.array([90, 255, 255])

    lower_red = np.array([-30, 0, 0])
    upper_red = np.array([30, 255, 255])

    # Threshold the HSV image to get only red colors
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
    red_channel = cv2.bitwise_and(frame, frame, mask=red_mask)
    blue_channel = cv2.bitwise_and(frame, frame, mask=blue_mask)
    green_channel = cv2.bitwise_and(frame, frame, mask=green_mask)

    cv2.imshow('frame', frame)
    cv2.imshow('red', red_channel)
    cv2.imshow('blue', blue_channel)
    cv2.imshow('green', green_channel)

    # Press Esc to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

camera.release()
cv2.destroyAllWindows()
