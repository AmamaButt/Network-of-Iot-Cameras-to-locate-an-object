import numpy as np

import cv2
img0= cv2.imread('images.jpg')  
img = cv2.imread('images.jpg',0)     #gray scale conversion     
img1=cv2.imwrite('gray_image.png', img)
ret,thresh_img = cv2.threshold(img,127,255 ,cv2.THRESH_BINARY) #binary conversion  
cv2.imshow('original',img0) 
cv2.imshow('gray',img) #display grayscale image
cv2.imshow('binary',thresh_img)    

im2, contours, hierarchy = cv2.findContours(thresh_img,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #contouring
cv2.drawContours(thresh_img, contours,-1, (255,255,255), 6) # displaying contouring
cv2.imshow('contour',thresh_img)   
cv2.waitKey(0)
cv2.destroyAllWindows()
