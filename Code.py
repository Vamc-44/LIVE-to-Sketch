#Live_sketch_drawing_using_python_opencv

#importing opencv for image and video classification and numpy for using arrays for storing image size

import cv2
import numpy as np

#code for sketch function part

def sketch(image):
    height = int(image.shape[0])                                 #height and width of the image
    width = int(image.shape[1])

    dim = (width,height)                                         #storing the dimmensions of image 

    resize = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)  #resize(src,dsize,interpolation=...) 

    kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
                                                                #kernel is used for convolution between the image 
                                                                # to filter,sharpen,etc

    sharpen = cv2.filter2D(resize,-1,kernel)                  #filter2d(src,ddepth,kernel) is used to sharpen the image

    gray = cv2.cvtColor(sharpen, cv2.COLOR_BGR2GRAY)          # converting into gray scale
    inv = 255-gray                                            #total 266 pixels            

    blur = cv2.GaussianBlur(inv,(15,15),sigmaX=0,sigmaY=0)
                                                              #GaussianBlur(src,ksize,sigmaX,sigmaY) gives the image 
                                                              # a low-pass filter that removes high-frequency component
                                           
    s = cv2.divide(gray,255-blur,scale=256)   #drawing sketch
    return s

#calling the sketch function

cap = cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()
    
    cv2.imshow("Live_Sketch",sketch(frame))
    cv2.imshow("Live_image",frame)
    
    if cv2.waitKey(1)==ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
