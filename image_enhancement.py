import numpy as np
import cv2

img=cv2.imread("i1.jpg",1)
cv2.imshow("image",img)
cv2.waitKey(0)
img_scaled = cv2.resize(img,None,fx=1.2,fy=1.2)
cv2.imshow('scaling-linear Interpolation ',img_scaled)
cv2.waitKey(0)

#Converting image to LAB Color model 
lab= cv2.cvtColor(img_scaled, cv2.COLOR_BGR2LAB)
cv2.imshow("lab",lab)
cv2.waitKey(0)


#Splitting the LAB image to different channels
l, a, b = cv2.split(lab)
cv2.imshow('l_channel', l)
cv2.waitKey(0)
cv2.imshow('a_channel', a)
cv2.waitKey(0)
cv2.imshow('b_channel', b)
cv2.waitKey(0)
#Applying CLAHE to L-channel
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
cl = clahe.apply(l)
cv2.imshow('CLAHE output', cl)
cv2.waitKey(0)

#Merge the CLAHE enhanced L-channel with the a and b channel
limg = cv2.merge((cl,a,b))
cv2.imshow('limg', limg)
cv2.waitKey(0)

#Converting image from LAB Color model to RGB model
final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
cv2.imshow('final', final)
cv2.waitKey(0)
cv2.destroyAllWindows()
