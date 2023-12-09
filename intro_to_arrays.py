import numpy as np
from imageio import imread, imwrite

image = imread("boring_rectangle.bmp")

image[50,:,:] = 100
image[:,100,:] = 100

imwrite("still_boring_rectangle.bmp", image)
