# Imports
from os import path
import glob
import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

def getSortedImageFiles(imageDir, imageFilePattern):    
    imageFileNames = glob.glob( path.join(imageDir, imageFilePattern) ) # find all files with this name pattern

    slideNumbers = [] # empty list to put slide numbers in 


    # Loop over all image file names and extract their slide number
    for ifn in imageFileNames:
        slideNumber = int(ifn.split('Slide')[1].split('.')[0])
        slideNumbers.append(slideNumber)

    # Sort the slide numbers numerically from smallest to largest, and use this to sort filenames
    slideNumbers = np.array(slideNumbers)
    imageFileNames = np.array(imageFileNames)
    sortIdx = np.argsort(slideNumbers)
    imageFileNames = imageFileNames[sortIdx]

    return imageFileNames

def getCircleCenter(imageFile):
    image = cv2.imread(imageFile)

    image_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

    circles = cv2.HoughCircles(image_gray,cv2.HOUGH_GRADIENT,1,20,
                     param1=60,param2=40,minRadius=0,maxRadius=0)

    return circles.flatten()[0:2] # (x,y)

if __name__ == "__main__": # do this stuff only if this is your main script
    imageDir = "moving_ball" # Define folder with all the images
    imageFilePattern = "Slide*.PNG"
    radiusCoordinates = []
    finalDistances = []

    imageFileNames = getSortedImageFiles(imageDir, imageFilePattern)
    # print(imageFileNames)

    for imageFile in imageFileNames:
        CircleCenter = getCircleCenter(imageFile)
        # print(getCircleCenter(imageFile))
        radiusCoordinates.append(CircleCenter)
    
    for i in range(1, len(radiusCoordinates)):
        finalDistances.append( math.dist(radiusCoordinates[i-1],radiusCoordinates[i]) )

    # print([f"{d:.2f}" for d in finalDistances])
    

    radiusCoordinates = np.array(radiusCoordinates)
    fig, ax = plt.subplots()
    ax.plot( radiusCoordinates[:,0], 
            radiusCoordinates[:,1],
            marker="o",
            markersize=20,
            markerfacecolor="tab:red",
            markeredgecolor="tab:green",
            linestyle="--",
            linewidth=2,
            color="k")

    ax.set_xlim([0,1280])
    ax.set_ylim([720,0])
    ax.grid(axis="both")
    ax.set_aspect("equal")
    plt.show()