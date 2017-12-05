
# coding: utf-8

# Cow Detection Algorithm. :)

# In[ ]:

from os import listdir
from os.path import isfile, join

import cv2
import numpy as np
import time
import collections

cap = cv2.VideoCapture(0)

# Load our image template, this is our reference image
#image_template = cv2.imread('images/cow_references/cow_a.jpg', 0) 
#image_template2 = cv2.imread('images/cow_references/cow_b.jpg', 0)
#image_template3 = cv2.imread('images/cow_references/cow_c.jpg', 0)

frame_count = 0

MIN_CONFIDENCE = 4

mypath = 'imagemodels/rmodels'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

if(len(onlyfiles) > 0):
    templs = []
    for fil in onlyfiles:
        templs.append(cv2.imread('imagemodels/rmodels/' + fil, 0))

the_temps = templs

def comparetemps(tempps,orig_feed,index):
    
    mx_data = sift_detector(orig_feed, tempps)
    # Our threshold to indicate object deteciton
    # We use 10 since the SIFT detector returns little false positves
    threshold = 15
    
    if mx_data >= threshold:
        return onlyfiles[index]
    else:
        return None

def sift_detector(new_image, image_template):
    
    # Function that compares input image to template
    # It then returns the number of SIFT matches between them
    
    image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
    image2 = image_template
    
    # Create SIFT detector object
    sift = cv2.SIFT(200)

    # Obtain the keypoints and descriptors using SIFT
    keypoints_1, descriptors_1 = sift.detectAndCompute(image1, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(image2, None)

    # Define parameters for our Flann Matcher
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 3)
    search_params = dict(checks = 100)

    # Create the Flann Matcher object
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # Obtain matches using K-Nearest Neighbor Method
    # the result 'matchs' is the number of similar matches found in both images
    matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

    # Store good matches using Lowe's ratio test
    good_matches = []
    for m,n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m) 

    return len(good_matches)

while True:
    
    frame_count = frame_count + 1
    
    curr_frame_ind = frame_count % 6

    #cv2.rectangle(frame,pointsX[curr_frame_ind],pointsY[curr_frame_ind], 255, 3) #A
    
    # Get webcam images
    ret, frame = cap.read()
    
    frame = cv2.pyrDown(frame)
    
    frame2 = frame.copy()
    
    # Get height and width of webcam frame
    height, width = frame.shape[:2]

    # Define ROI Box Dimensions
    #top_left_x = width / 3
    #top_left_y = (height / 2) + (height / 4)
    #bottom_right_x = (width / 3) * 2
    #bottom_right_y = (height / 2) - (height / 4)
    
    # Define ROI Box Dimensions
    top_left_x = 0 #width / 3
    top_left_y = 0 #(height / 2) + (height / 4)
    bottom_right_x = (width / 3)
    bottom_right_y = (height / 2)
    
    # Draw rectangular window for our region of interest       
    pointsX = [(top_left_x,top_left_y),(bottom_right_x,top_left_y),(bottom_right_x*2,top_left_y),(top_left_x,bottom_right_y),(bottom_right_x,bottom_right_y),(bottom_right_x*2,bottom_right_y)]
    pointsY = [(bottom_right_x,bottom_right_y), (bottom_right_x*2,bottom_right_y),(bottom_right_x*3,bottom_right_y),(bottom_right_x,bottom_right_y*2),(bottom_right_x*2,bottom_right_y*2),(bottom_right_x*3,bottom_right_y*2)]
    
    # Draw rectangular window for our region of interest   
    cv2.rectangle(frame2, pointsX[curr_frame_ind], pointsY[curr_frame_ind], 255, 3)
    
    cropped1 = frame[top_left_x:bottom_right_y , top_left_y:bottom_right_x]
    cropped2 = frame[top_left_x:bottom_right_y , bottom_right_x:bottom_right_x*2]
    cropped3 = frame[top_left_x:bottom_right_y , bottom_right_x*2:bottom_right_x*3]
    
    cropped4 = frame[bottom_right_y:bottom_right_y*2 , top_left_x:bottom_right_x]
    cropped5 = frame[bottom_right_y:bottom_right_y*2 , bottom_right_x:bottom_right_x*2]
    cropped6 = frame[bottom_right_y:bottom_right_y*2 , bottom_right_x*2:bottom_right_x*3]
    
    crops = [cropped1,cropped2,cropped3,cropped4,cropped5,cropped6]
    # Crop window of observation we defined above
    cropped = crops[curr_frame_ind] #frame[bottom_right_y:top_left_y , top_left_x:bottom_right_x]
    
    # Flip frame orientation horizontally
    #frame = cv2.flip(frame,1)
    txt_x,txt_y = pointsX[curr_frame_ind]
    
    cv2.putText(frame2,'Scanning...',(txt_x,txt_y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5 ,(0,255,0), 2)
    
    index = 0
    
    detectedlist = []
    
    for temp in the_temps:
        result = comparetemps(temp,cropped,index)
        index = index + 1
        
        if not result is None:
            detectedlist.append(result)
    
    if(len(detectedlist)> 0):
        has_detected = True
        
        cow_names = []
        
        cv2.putText(frame,'Detected:',(10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5 ,(0,255,0), 2)
        for item in detectedlist:
            cv2.rectangle(frame, pointsX[curr_frame_ind], pointsY[curr_frame_ind], (0,255,0), 3)
            cow_names.append(item[:4])
        
        counter = collections.Counter(cow_names)
        
        cow_count = counter.values()
        cow_n = counter.keys()
        
        cnc = 0 #cow name counter, for iterating through the cow counts
        
        linebreak = 8
        
        for cn in cow_n:
            cv2.putText(frame,cn + ":" + str(cow_count[cnc]),(10,20+20+linebreak), cv2.FONT_HERSHEY_SIMPLEX, 0.5 ,(0,255,0), 2)
            cnc = cnc + 1
            linebreak = linebreak + 10
        
        if not cow_count is None:
            if not cow_n is None:
                print(cow_count)
                print(cow_n)
    else:
        has_detected = False
    
    
    # Get number of SIFT matches
    #matches = sift_detector(cropped, image_template)
    #matches2 = sift_detector(cropped, image_template2)
    #matches3 = sift_detector(cropped, image_template3)

    # Display status string showing the current no. of matches 
    #cv2.putText(frame,str(matches),(450,450), cv2.FONT_HERSHEY_COMPLEX, 2,(0,255,0),1)
    
    # Our threshold to indicate object deteciton
    # We use 10 since the SIFT detector returns little false positves
    #threshold = 10
    
    #has_detected = False

    #if matches > threshold:
        #has_detected = True
        #cv2.rectangle(frame, pointsX[curr_frame_ind], pointsY[curr_frame_ind], (0,255,0), 3)
        #cv2.putText(frame,'COW A Found',(txt_x,txt_y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5 ,(0,255,0), 2)
    #elif matches2 > threshold:
        #has_detected = True
        #cv2.rectangle(frame, pointsX[curr_frame_ind], pointsY[curr_frame_ind], (0,255,0), 3)
        #cv2.putText(frame,'COW B Found',(txt_x,txt_y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5 ,(0,255,0), 2)
    #elif matches3 > threshold:
        #has_detected = True
        #cv2.rectangle(frame, pointsX[curr_frame_ind], pointsY[curr_frame_ind], (0,255,0), 3)
        #cv2.putText(frame,'COW C Found',(txt_x,txt_y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5 ,(0,255,0), 2)
    
    if has_detected:
        cv2.imshow('Cow Detection', frame)
    else:
        cv2.imshow('Cow Detection', frame2)
    
    cv2.imshow("Detection Region",cropped)
    #time.sleep(0.006)
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()   


# In[ ]:




# #### Flannbased matching is quite fast, but not the most accurate. Other matching methods include:
# 
# - BruteForce
# - BruteForce-SL2 (not in the documentation, BUT this is the one that skeeps the squared root !)
# - BruteForce-L1
# - BruteForce-Hamming
# - BruteForce-Hamming(2)
# 

# ## Object Detection using ORB

# In[22]:

import cv2
import numpy as np


def ORB_detector(new_image, image_template):
    # Function that compares input image to template
    # It then returns the number of ORB matches between them
    
    image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)

    # Create ORB detector with 1000 keypoints with a scaling pyramid factor of 1.2
    orb = cv2.ORB(1000, 1.2)

    # Detect keypoints of original image
    (kp1, des1) = orb.detectAndCompute(image1, None)

    # Detect keypoints of rotated image
    (kp2, des2) = orb.detectAndCompute(image_template, None)

    # Create matcher 
    # Note we're no longer using Flannbased matching
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Do matching
    matches = bf.match(des1,des2)

    # Sort the matches based on distance.  Least distance
    # is better
    matches = sorted(matches, key=lambda val: val.distance)

    return len(matches)

cap = cv2.VideoCapture('rstp://192.168.1.168:554')

# Load our image template, this is our reference image
image_template = cv2.imread('images/cow_references', 0) 
# image_template = cv2.imread('images/kitkat.jpg', 0) 

while True:

    # Get webcam images
    ret, frame = cap.read()
    
    # Get height and width of webcam frame
    height, width = frame.shape[:2]

    # Define ROI Box Dimensions (Note some of these things should be outside the loop)
    top_left_x = width / 3
    top_left_y = (height / 2) + (height / 4)
    bottom_right_x = (width / 3) * 2
    bottom_right_y = (height / 2) - (height / 4)
    
    # Draw rectangular window for our region of interest
    cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), 255, 3)
    
    # Crop window of observation we defined above
    cropped = frame[bottom_right_y:top_left_y , top_left_x:bottom_right_x]

    # Flip frame orientation horizontally
    frame = cv2.flip(frame,1)
    
    # Get number of ORB matches 
    matches = ORB_detector(cropped, image_template)
    
    # Display status string showing the current no. of matches 
    output_string = "Matches = " + str(matches)
    cv2.putText(frame, output_string, (50,450), cv2.FONT_HERSHEY_COMPLEX, 2, (250,0,150), 2)
    
    # Our threshold to indicate object deteciton
    # For new images or lightening conditions you may need to experiment a bit 
    # Note: The ORB detector to get the top 1000 matches, 350 is essentially a min 35% match
    threshold = 350
    
    # If matches exceed our threshold then object has been detected
    if matches > threshold:
        cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), (0,255,0), 3)
        cv2.putText(frame,'Object Found',(50,50), cv2.FONT_HERSHEY_COMPLEX, 2 ,(0,255,0), 2)
    
    cv2.imshow('Object Detector using ORB', frame)
    
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()   


# In[ ]:



