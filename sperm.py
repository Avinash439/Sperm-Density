import numpy as np
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages') #since I am using python3 i have to do this.
import cv2
print("OpenCV Version: {}".format(cv2.__version__))
cap = cv2.VideoCapture("/home/avinash/mojointerviewhomework/mojo_video1.avi") #input Video File
property_id = int(cv2.CAP_PROP_FRAME_COUNT) 
length = int(cv2.VideoCapture.get(cap,property_id))
print("total number of frames:",length) #calculating the total no of frames in the given file.
sum=0

frame_width = int(cap.get(3)) 
frame_height = int(cap.get(4)) 
kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))# Applying 3*3 kernel with the structuring element
size = (frame_width, frame_height) 

result = cv2.VideoWriter("/home/avinash/ros_ws/src/data/age1.avi",  cv2.VideoWriter_fourcc(*'XVID'), 60, size,True) #saving the video file in the location 
while(cap.isOpened()):
    ret, frame = cap.read() #processing frame by frame in the while loop
    if frame is None: #if the frame is empty it will come out of loop.
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converting given RGB frame to gray as a part of preprocessing
    edges = cv2.Canny(gray,12,62)  # Applied canny edge filter on the gray image store as edges
    # erosion=cv2.erode(edges,kernel1,iterations=0)
    dilution=cv2.dilate(edges,kernel1,iterations=10) # done morphology technique of dilution adding some pixels to make it solid.
    # cv2.morphologyEx(dilution, cv2.MORPH_CLOSE, kernel1)
    contours, _ = cv2.findContours(dilution, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # up next found the boundaries by countours function.
    contour_area=[] # empty list for storing contour areas.

    for cnt in contours: # In order to find the area threshold, calculated boundary area for all the contours
        contour_area.append(cv2.contourArea(cnt)) # we send all the areas to the list

    areaTH=np.sum(contour_area)/len(contours) # we found the area threshold by summing all the contour areas divided by no of contours.
    

    for cnt in contours:
        area = cv2.contourArea(cnt) 
        if area > areaTH: #Based on the conditional statement if area of contour is greater than area threshold it will draw the contour

    
            ################
            #   Bounding box     #
            #################
            sum=sum+1 # the no of times it enters the loop is calculated as a sperm, so we add it.
            # ellipse = cv2.fitEllipse(cnt)
            # im = cv2.ellipse(dilution,ellipse,(0,0,0),2)        
            cv2.drawContours(frame, cnt, -1, (0,0,0), 3) # we draw the contours on the origial frame.
            
      
    result.write(frame) #saving the video file.

print("Contours_areas",contour_area)
print("sum",np.sum(contour_area))
print("length of Contours",len(contours))
print("Area Threshold",areaTH)    
print("Total no of sperms:",sum) # total no of sperms in the total video
print("No of sperms per frame:",round(sum/length)) # it prints the total no of sperms per frame.
cap.release()
cv2.destroyAllWindows()

