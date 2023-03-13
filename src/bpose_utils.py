import math
import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt


def cv2_imshow(img):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

def resize_and_show(img, desired_width, desired_height):
    h, w = img.shape[:2]
    
    if h < w:
        img = cv2.resize(img, (desired_width, math.floor(h / (w / desired_width))))
    else:
        img = cv2.resize(img, (math.floor(w / ( h / desired_height)), desired_height))
    
    cv2_imshow(img)

    return img

