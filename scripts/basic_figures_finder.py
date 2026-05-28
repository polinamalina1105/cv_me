import cv2
import numpy as np

image = cv2.imread("./images/shapeMultiFind/097.jpg")

def find_nearest_color(px, vocab):
    min_dist = float('inf')
    nearest_col = ''
    for key, value in colors.items():
        dist = np.linalg.norm(np.array(px) - np.array(key))
        if dist < min_dist:
            min_dist = dist
            nearest_col = vocab[key]
    return nearest_col

colors = {(255,255,255):"white",
          (0,0,255):"red",
          (0,255,0):"green",
          (255,0,0):"blue",
          (0,255,255):"yellow",
          (255,0,255):"purple",
          (255,255,0):"aqua"}

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img_bin = np.where(img_gray > 15, 255, 0).astype(np.uint8)

cont, hierarchy = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(cont)):
    x, y, w, h = cv2.boundingRect(cont[i])
    x_center = x + w // 2
    y_center = y + h // 2
    bound = img_bin[y:y+h, x:x+w]
    if np.mean(bound) < 150:
        shape = 'triangle'
    elif np.mean(bound) > 240:
        shape = 'square'
    else:
        shape = 'circle'
    color = find_nearest_color(image[y_center, x_center], colors)
    print(f'{(x_center, y_center)} - {color} {shape}')