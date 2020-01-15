import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('hhe.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) 

plt.imshow(res)
plt.axis('off')
plt.text(131, 348, r'Original Image')
plt.text(506, 348, r'Historgram Equalization')
plt.show()
