#client.py

import socket                   # Import socket module
import cv2
import time
import math
from math import hypot
from PIL import Image
import numpy as np
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60002                   # Reserve a port for your service.
s.connect((host, port))
data="hello server!"
s.send(data.encode())
with open('received_file', 'wb') as l:
  while True:
# write data to a file
    g = s.recv(1024)
    print('g=%s', (g))
    if not g:
      break
    l.write(g)
    print(g)
   
    im = Image.open("received_file")
    rgb_im = im.convert('RGB')
    rgb_im.save('multi2.jpg')
    image=cv2.imread("multi2.jpg")
    image1=cv2.imread("multi2.jpg")
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(image, 10, 250)
    (,cnts, ) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image,cnts,-1,[0,255,0],2)
    #  cv2.imshow('Contours',image)
    idx = 0
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if w>15 and h>30:
            idx+=1
            new_img=image1[y:y+h,x:x+w]
            cv2.imwrite(str(idx) + '.png', new_img)
            maxarea=0
            maxlength=0
            maxwidth=0
            img=cv2.imread('multi2.jpg')
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            _,thresh=cv2.threshold(gray,140,255,cv2.THRESH_BINARY_INV)
            thresh=cv2.GaussianBlur(thresh,(5,5),0)
            , contours,  = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(img,contours,-1,(0,0,0),2)
            i=0
            for c in contours:
                cnt = contours[i]
                M = cv2.moments(cnt)
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect) 
                box = np.int0(box)
                points=[]
                for p in box:
                    pt = (p[0],p[1])
                    cx=int(p[0])
                    cy=int(p[1])
                    cv2.circle(img,(cx,cy),2,(0,255,0),2) 
                    points.append(cx)
                    points.append(cy)
                cv2.drawContours(img,[box],0,(0,0,255),2)
                width=math.sqrt( (points[0] - points[2])**2 + (points[1] - points[3])**2 )
                length=math.sqrt( (points[0] - points[6])**2 + (points[1] - points[7])**2 )
                area=length*width
                if i == 0:
                    maxarea=area
                    maxlength=length
                    maxwidth=width
                if area>maxarea:
                    maxarea=area
                    maxlength=length
                    maxwidth=width
                i=i+1
            #print("maxlength  ", maxlength)
            #print("maxwidth  ", maxwidth)      
            #print("maxarea",maxarea)
            Ratio=maxlength/maxwidth
            print(Ratio)
            #print(Ratio)
            if Ratio<=2.0:
                print("          ***** Image is Of Cup *****")
                cup="          ***** Image is Of Cup *****"
                s.send(cup.encode())
            if Ratio>2.0:
                print("          ****** Image is Of Pencil*****")
                pencil="          ****** Image is Of Pencil*****"
                s.send(pencil.encode())
l.close()  
print('Successfully get the file')
s.close()
print('connection closed')