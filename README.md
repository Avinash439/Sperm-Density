# Sperm-Density
Computer Vision to determine sperm density
___
## Description
This repository contains necessary code to allow the program to estimate the number of sperms from a video file.
___
### Prerequisites

Things you need to install the software and how to install them


```
Linux environment(ubuntu 16.04 LTS).
Python3
OpenCV 4.3.0 

```
___
### Installing

Make sure that you have [Python3 installed](https://realpython.com/installing-python/) on your machine.

```
sudo apt-get install python3
sudo apt-get install python3-pip
```
Step:2 Installing opencv in your computer.

```
pip3 install opencv-python
```
___
### Summary of code file.

The algorithm will work on a video file of 'n' images, where n is the integer value. A higher 'n' value means more number of images which takes some time for computation. For each image following steps are done to segment sperms and count them.

- First, as sperm images are read in RGB format, then they will be converted to grayscale.
- I have choosen edge detection and contours because there are no colour or texture features.
- Next, by using canny edge detector I found edges of grayscale image,is so choosen that all edge elements are preserved and noise is eliminated.
- In order to make the sperm fully connected with out any breaks, I am using morphology technique dilation with structuring element and kernel for adding some pixels to sperms in order to preserve sperm boundaries.Morphology will ensue to the sperms that are  well-formed will be included in counting.
- From the output of dilated image I am finding the contours, can be explained simply as a curve joining all the continuous points along the boundary, having same color or intensity. The contours are a useful tool for shape analysis and object detection and recognition.
- Based on the number of detected contours I am calculating the contour area for all the contours and finding the threshold area by summing all the contour areas divided by total number of contours from the input video file.Threshold plays a vital role in finding the number of sperms count.
- Finally with the help of contour area greater than the area threshold I am counting that as a sperm and drawing the contours on the original image.


___

### Summary of Deep Learning approach

Deep neural networks can be another approach for finding the sperm count. It is capable of finding high-dimensional features from the input data. Now a days Deep neural networks are being used in various domains of science. Some of the convolutional neural network architecture based object detectors such as R-CNN, SSD, YOLO, RetinaNet can be used to solve this problem after transfer learning.

CNN's attempts to extract features from the input image and based on features it detects the object. Sperms are small objects with few attributes like brightness, the special shape of head and tail, and motility Which helps to distinguish the sperms. 




