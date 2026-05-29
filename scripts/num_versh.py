import cv2
import numpy as np

image = cv2.imread('./images/shapeMultiFind/097.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_bin = cv2.inRange(image_gray, 20, 255)
contours, hierarchy = cv2.findContours(image_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    num_points = len(approx)
    print(f'количество вершин: {num_points}')