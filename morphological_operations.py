import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('m2.png',0)
fig=plt.figure()
plt.subplot(1,3,1)
plt.imshow(img)
plt.axis('off')
plt.text(11, 170, r'Original Image')

kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)
plt.subplot(1,3,2)
plt.imshow(erosion)
plt.axis('off')
plt.text(37, 170, r'Erosion')

dilation = cv.dilate(img,kernel,iterations = 1)
plt.subplot(1,3,3)
plt.imshow(dilation)
plt.axis('off')
plt.text(37, 170, r'Dilation')
#plt.text(37, 170, r'Dilation')

plt.show()
