#Image to image skecth using OpenCV with python

import cv2
import numpy as np

img = cv2.imread("me.jpeg")


width = 350
height = 440
dim = (width, height)                                        

resize = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)   

kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
                                                                 
sharpen = cv2.filter2D(resize,-1,kernel)                  

gray = cv2.cvtColor(sharpen, cv2.COLOR_BGR2GRAY)          
inv = 255-gray                                                        

blur = cv2.GaussianBlur(inv,(15,15),sigmaX=0,sigmaY=0)
                                                              
s = cv2.divide(gray,255-blur,scale=256)

cv2.imshow("Sketch_Image",s)
cv2.waitKey(0)
cv2.destroyAllWindows()
