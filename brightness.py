import cv2
import numpy as np

img = cv2.imread("15.png", cv2.IMREAD_COLOR)
original = cv2.resize(img, (350,350))

alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
# Simple contrast control
beta = int(input('Enter the beta value [0-100]: '))
# Simple brightness control

mul_img = cv2.multiply(img, np.array([alpha]))
# mul_img = img*alpha
new_img = cv2.add(mul_img, beta)
# new_img = img*alpha + beta 

hsv = cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(15,15))

hsv[:,:,0] = clahe.apply(hsv[:,:,0])
hsv[:,0,:] = clahe.apply(hsv[:,0,:])
hsv[0,:,:] = clahe.apply(hsv[0,:,:])

#cl1 = clahe.apply(new_img)

img_output = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
#frame = cv2.addWeighted(img_output, 1.5, frame, -0.5, 0, frame)

kernel = np.array([[-1, -1, -1],
                   [-1, 8.5, -1],
                   [-1, -1, -1]])

filt = cv2.filter2D(img_output, -1, kernel)


cv2.imshow('original',img)
cv2.imshow('step 1',new_img)
cv2.imshow('step 2',hsv)
cv2.imshow('step 3',img_output)
cv2.imshow('step 4',filt)

cv2.waitKey(0)
cv2.destroyAllWindows()


