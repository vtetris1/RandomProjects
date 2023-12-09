import numpy as np
from imageio import imread, imwrite

image = imread("eraser.jpg")

blueSlice = image[:,:,2].copy()
image[:,:,2] = 0
image[:,:,1] = blueSlice

imwrite("weird_eraser.jpg", image)