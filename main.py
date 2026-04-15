import cv2
import numpy as np
import matplotlib.pyplot as plt


def denoise_image(image_path):
    noisy_image = cv2.imread(imaage_path)
    noisy_image = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB)
