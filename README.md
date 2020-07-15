# Sperm-Density
Computer Vision to determine sperm density
___
## Description
This repository contains necessary code to allow the program to estimate the number of sperm in a video file.
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

The algorithm will work on a video file of n images, where n is the integer value. A higher n value means more number of images which takes some time for computation. For each image following steps are done to segment sperms and count them.

Item 1.First, as sperm images are read in RGB format, then they will be converted to grayscale.
Item 2.Next, by using canny edge detector we will find edges of grayscale image,is so choosen that all edge elements are preserved and noise is eliminated.
Item 3.In order to make the sperm fully connected with out any breaks, I am using morphology technique dilution with structuring element and kernel for adding some pixels to sperms in order to preserve sperm boundaries.Morphology will ensue to the sperms that are  well-formed will be included in counting.
Item 4.



