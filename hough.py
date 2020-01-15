import cv2
import numpy as np

img = cv2.imread('sudoku.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

rho = input("Set the pho accuracy (1 for best)")
theta = input("How much degree of accuracy? (180 for best)")
lines = cv2.HoughLines(edges,float(rho),np.pi/float(theta),200)

for i in range (0,31):
    for rho,theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    
cv2.imshow("P", img)
cv2.imwrite('houghlines3.jpg',img)
cv2.waitKey(0)
