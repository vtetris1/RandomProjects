from imageio import imread, imwrite
from matplotlib import colors
import numpy as np

print()

def findColumns(image):
    x = 0

    while image[:,x,0].all(): # while all pixels in this column are white (>0 = True)
        x = x + 1
    x_left = x - 1

    while not image[:,x,0].all(): # while not all pixels in this column are white (>0 = True)
        x = x + 1
    x_right = x

    return x_left, x_right



def findRows(image):
    x = 0
    
    while image[x,:,0].all(): # while all pixels in this row are white (>0 = True)
        x = x + 1
    x_top = x - 1

    while not image[x,:,0].all(): # while not all pixels in this row are white (>0 = True)
        x = x + 1
    x_bottom = x

    return x_top, x_bottom 

def drawCross(image, x_left, x_right, x_top, x_bottom, rgb=[100,100,100]):
    x_middle_col = round( (x_left + x_right) / 2 )
    x_middle_row = round( (x_top + x_bottom) / 2 )

    r,g,b = rgb
    image[:,x_middle_col,0] = r
    image[:,x_middle_col,1] = g
    image[:,x_middle_col,2] = b

    image[x_middle_row,:,0] = r
    image[x_middle_row,:,1] = g
    image[x_middle_row,:,2] = b
    return

def drawBorder(image, x_left, x_right, x_top, x_bottom, color='bright green'):
    rgb = np.array(colors.to_rgb('xkcd:'+color)) * 255
    image[x_top,x_left:x_right+1,:] = rgb
    image[x_bottom,x_left:x_right+1,:] = rgb

    image[x_top:x_bottom+1,x_right,:] = rgb
    image[x_top:x_bottom+1,x_left,:] = rgb


def drawAll(image):
    x_left, x_right = findColumns(image)
    x_top, x_bottom = findRows(image)
        
    drawBorder(image, x_left, x_right, x_top, x_bottom, color='lime green')
    drawCross(image, x_left, x_right, x_top, x_bottom, rgb=[200,100,0])


image = imread("boring_rectangle.bmp")
drawAll(image)
imwrite("testing_rectangle.bmp", image)
