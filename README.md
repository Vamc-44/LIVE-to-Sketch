# LIVE-to-Sketch

A simple computer vision program used to convert the  live webcam videio or image to the respective sketch.

We use OpenCV with python to write the script for live sketch. Since OpenCV makes us easy to work with images and videos on the computer. We also use Numpy library.

In image processing, it happens by going through each pixel to perform a calculation with the pixel and its neighbours. The kernels will define the size of the convolution, the weights applied to it, and an anchor point usually positioned at the center.
Applying the sharpening filter will sharpen the edges in the image. This filter is very useful when we want to enhance the edges in an image that's not crisp.
In Gaussian Blur operation, the image is convolved with a Gaussian filter instead of the box filter. The Gaussian filter is a low-pass filter that removes the high-frequency components are reduced.

**Output of the Program**

*Input Image/Live image

<img src="https://user-images.githubusercontent.com/91316387/176991378-b25a4ae5-145b-4a83-89ee-2b075c192801.png" align="centre" width="350" height="350">

*Output image/Skecth image

![image](https://user-images.githubusercontent.com/91316387/176991772-8a56564b-44f0-4ef7-b628-460b7bdb62a5.png)


