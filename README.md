# LIVE-to-Sketch

A simple computer vision program used to convert the  live webcam videio or image to the respective sketch.

We use OpenCV with python to write the script for live sketch. Since OpenCV makes us easy to work with images and videos on the computer. We also use Numpy library.

In image processing, it happens by going through each pixel to perform a calculation with the pixel and its neighbours. The kernels will define the size of the convolution, the weights applied to it, and an anchor point usually positioned at the center.
Applying the sharpening filter will sharpen the edges in the image. This filter is very useful when we want to enhance the edges in an image that's not crisp.
In Gaussian Blur operation, the image is convolved with a Gaussian filter instead of the box filter. The Gaussian filter is a low-pass filter that removes the high-frequency components are reduced.

**Output of the Program**

*Input Image/Live image

<img src="https://user-images.githubusercontent.com/91316387/176991378-b25a4ae5-145b-4a83-89ee-2b075c192801.png" align="centr" width="100" height="100">

*Output image/Skecth image

<img src="https://user-images.githubusercontent.com/91316387/176991386-f7d22ba4-04ef-4114-b04b-55e459ed821e.pn" align="centr" width="100" height="100">
