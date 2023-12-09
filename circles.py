import cv2
import numpy as np

# Read image
img = cv2.imread('some_black_circles.bmp')

img_copy = img.copy()

# Convert to greyscale
img_gray = cv2.cvtColor(img_copy,cv2.COLOR_RGB2GRAY)

# Apply Hough transform to greyscale image
circles = cv2.HoughCircles(img_gray,cv2.HOUGH_GRADIENT,1,20,
                     param1=60,param2=40,minRadius=0,maxRadius=0)

print(circles)

circles = np.uint16(np.around(circles))
# Draw the circles
for circleInfo in circles[0,:]:
    pass
    # # draw the outer circle
    # cv2.circle(img,(i[0],i[1]),i[2],(0,0,255),2)
    # # draw the center of the circle
    # cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    
cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()