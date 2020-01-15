import numpy
import cv2
import math
import matplotlib.pyplot as plt

#IMAGE 1

img = cv2.imread('i3.jpg')
cv2.imshow('img', img)

blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('g1', blur)
median = cv2.medianBlur(img,5)
cv2.imshow('m1', median)

def psnr(img1, img2):
     mse = numpy.mean( (img1 - img2) ** 2 )
     if mse == 0:
          return 100
     PIXEL_MAX = 255.0
     return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

d=psnr(img,blur)
print("The value of PSNR for guassian blur on image 1 is", d)

e=psnr(img,median)
print("The value of PSNR for median blur on image 1 is", e)

cv2.waitKey(0)
cv2.destroyAllWindows()

#IMAGE 2

img2 = cv2.imread('otherNoisyImage.jpg')
cv2.imshow('img2', img2)


blur = cv2.GaussianBlur(img2,(5,5),0)
cv2.imshow('g2', blur)
e=psnr(img2,blur)
print("The value of PSNR for median blur on image 2 is", e)

median = cv2.medianBlur(img2,5)
cv2.imshow('m2', median)
e=psnr(img2,median)
print("The value of PSNR for median blur on image 2 is", e)

cv2.waitKey(0)
cv2.destroyAllWindows()


#IMAGE 3
img3 = cv2.imread('noisyImage3.jpg')
cv2.imshow('img3', img3)

blur = cv2.GaussianBlur(img3,(5,5),0)
cv2.imshow('g3', blur)
e=psnr(img3,blur)
print("The value of PSNR for median blur on image 3 is", e)

median = cv2.medianBlur(img3,5)
cv2.imshow('m3', median)
e=psnr(img3,median)
print("The value of PSNR for median blur on image 3 is", e)

cv2.waitKey(0)
cv2.destroyAllWindows()





