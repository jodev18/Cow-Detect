import cv2
import numpy as np
import time
from FinalProductionCode.SMSSender import SMSSender
from FinalProductionCode.DatabaseManager import DBManager
from datetime import datetime
import urllib2

#detection algorithm using sift
def sift_detector(new_image, image_template):
    # Function that compares input image to template
    # It then returns the number of SIFT matches between them

    image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY) # change to grayscale
    image2 =  cv2.cvtColor(image_template, cv2.COLOR_BGR2GRAY)

    # Create SIFT detector object
    sift = cv2.SIFT(180) # limit to 180 features for perfomance

    # Obtain the keypoints and descriptors using SIFT
    keypoints_1, descriptors_1 = sift.detectAndCompute(image1, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(image2, None)

    # Define parameters for our Flann Matcher
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=3)
    search_params = dict(checks=100)

    # Create the Flann Matcher object
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # Obtain matches using K-Nearest Neighbor Method
    # the result 'matchs' is the number of similar matches found in both images
    matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

    # Store good matches using Lowe's ratio test
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    return len(good_matches)


frame_count = 0


def check_pumatong(pumatong, pinatungan):
    if pumatong != pinatungan:
        patong_info = []
        cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 3)
        cv2.putText(frame, pumatong + " and " + pinatungan + " are having it.", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (0, 255, 0), 1)
        patong_info.append(pumatong)
        patong_info.append(pinatungan)
        print(pumatong + "=>" + pinatungan)
        return patong_info
    else:
        return None



cap = cv2.VideoCapture(0)

# Load our image template, this is our reference image
image_template = cv2.imread('imagemodels/COW_A.jpg', 0)
image_template2 = cv2.imread('imagemodels/COW_B.jpg', 0)
image_template3 = cv2.imread('imagemodels/COW_C.jpg', 0)
image_template4 = cv2.imread('imagemodels/COW_D.jpg', 0)

#For the SMS and database stuff..
sms_handler = SMSSender()
db_handler = DBManager()

cowA = "COW A"
cowB = "COW B"
cowC = "COW C"
cowD = "COW D"

previous_detect = None
current_detect = None
third_stack = None

sec_count = 0

may_pumatong = False
has_drawn_already = False

start = time.time()

host = "192.168.1.9:8080"
#if len(sys.argv)>1:
#    host = sys.argv[1]

hoststr = 'http://' + host + '/video'
stream=urllib2.urlopen(hoststr)
bytes=''


while True:

    curr_date = datetime.now().date()
    curr_time = datetime.now().time()

    frame_count = frame_count + 1
    curr_frame_ind = frame_count % 6
    sec_trigger = frame_count % 30

    bytes += stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a != -1 and b != -1:
        jpg = bytes[a:b + 2]
        bytes = bytes[b + 2:]
        frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)

        #cv2.imshow("rawstream",frame)
    # Get webcam images
    #ret, frame = cap.read()
        print("Handling stream")

        height, width = frame.shape[:2]

        # Define ROI Box Dimensions
        top_left_x = 0  # width / 3
        top_left_y = 0  # (height / 2) + (height / 4)
        bottom_right_x = (width / 3)
        bottom_right_y = (height / 2)

        # Draw rectangular window for our region of interest
        pointsX = [(top_left_x, top_left_y), (bottom_right_x, top_left_y), (bottom_right_x * 2, top_left_y),
                   (top_left_x, bottom_right_y), (bottom_right_x, bottom_right_y), (bottom_right_x * 2, bottom_right_y)]
        pointsY = [(bottom_right_x, bottom_right_y), (bottom_right_x * 2, bottom_right_y),
                   (bottom_right_x * 3, bottom_right_y), (bottom_right_x, bottom_right_y * 2),
                   (bottom_right_x * 2, bottom_right_y * 2), (bottom_right_x * 3, bottom_right_y * 2)]

        # Draw rectangular window for our region of interest
        cv2.rectangle(frame, pointsX[curr_frame_ind], pointsY[curr_frame_ind], 255, 3)

        ### WE CROP THE FRAME INTO 6 PARTS, TO IMPROVE EFFICIENCY OF DETECTION ##

        cropped1 = frame[top_left_x:bottom_right_y, top_left_y:bottom_right_x]
        cropped2 = frame[top_left_x:bottom_right_y, bottom_right_x:bottom_right_x * 2]
        cropped3 = frame[top_left_x:bottom_right_y, bottom_right_x * 2:bottom_right_x * 3]

        cropped4 = frame[bottom_right_y:bottom_right_y * 2, top_left_x:bottom_right_x]
        cropped5 = frame[bottom_right_y:bottom_right_y * 2, bottom_right_x:bottom_right_x * 2]
        cropped6 = frame[bottom_right_y:bottom_right_y * 2, bottom_right_x * 2:bottom_right_x * 3]

        crops = [cropped1, cropped2, cropped3, cropped4, cropped5, cropped6]

        cropped = crops[curr_frame_ind]

        # Crop window of observation we defined above
        #cropped = frame[bottom_right_y:top_left_y, top_left_x:bottom_right_x]

        # Flip frame orientation horizontally
        frame = cv2.flip(frame, 1)

        # Get number of SIFT matches
        #matches = sift_detector(cropped, image_template)
       # matches2 = sift_detector(cropped, image_template2)
        ##matches3 = sift_detector(cropped, image_template3)
        #matches4 = sift_detector(cropped, image_template4)

        # Display status string showing the current no. of matches
         cv2.putText(frame,str(matches),(450,450), cv2.FONT_HERSHEY_COMPLEX, 2,(0,255,0),1)

        # Our threshold to indicate object deteciton
        # We use 10 since the SIFT detector returns little false positves
        threshold = 10

        # If matches exceed our threshold then object has been detected
        #if not previous_detect is None:

         #   may_pumatong = True
    #
          #  db_info = []
          #  db_info.append(str(curr_time))
          #  db_info.append(str(curr_date))
          #  db_info.append(str('5:00'))


            # if(sec_trigger == 0):
            # sec_count = sec_count + 1
            # cv2.putText(frame,"Sec: " + str(sec_count),(200,450), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),1)

            #if matches > threshold:
              #  current_detect = cowA
             #   end = time.time()
                #cv2.putText(frame, "Elapsed: " + str(end - start), (200, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
             #   if (third_stack == current_detect):
                    # release ng patong
             #       sec_count = 0
              #      cv2.putText(frame, "RELEASED", (200, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
              #      may_pumatong = False
             #       third_stack = ""
              #  else:
              #      if not has_drawn_already:
              #          has_drawn_already = True
              #          if check_pumatong(current_detect, previous_detect) is not None:
              #              patong = check_pumatong(current_detect, previous_detect)
             #               db_info.append(patong[0])
              #              db_info.append(patong[1])

             #       else:
              #          has_drawn_already = False
              #      previous_detect = cowA
          #  elif matches2 > threshold:
              #  current_detect = cowB
              #  end = time.time()
                #cv2.putText(frame, "Elapsed: " + str(end - start), (200, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
             #   if (third_stack == current_detect):
                    # release ng patong
               #     may_pumatong = False
                #    sec_count = 0
                #    cv2.putText(frame, "RELEASED", (200, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)

                #    third_stack = ""
               # else:
                 #   if not has_drawn_already:
                  #      has_drawn_already = True
                  #      if check_pumatong(current_detect, previous_detect) is not None:
                  #          patong = check_pumatong(current_detect, previous_detect)
                  #          db_info.append(patong[0])
                  #          db_info.append(patong[1])
                 #   else:
                 #       has_drawn_already = False
                 #   previous_detect = cowB

           # elif matches3 > threshold:
             #   current_detect = cowC
            #    end = time.time()
            #    cv2.putText(frame, "Elapsed: " + str(end - start), (200, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
            #    if (third_stack == current_detect):
             #       may_pumatong = False
            #        # release ng patong
             #       sec_count = 0
             #       cv2.putText(frame, "RELEASED", (200, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)

               #     third_stack = ""
             #   else:
             #       if not has_drawn_already:
              #          has_drawn_already = True
              #          if check_pumatong(current_detect, previous_detect) is not None:
               #             patong = check_pumatong(current_detect, previous_detect)
               #             db_info.append(patong[0])
               #             db_info.append(patong[1])
               #     else:
               #         has_drawn_already = False
               #     previous_detect = cowC

           # elif matches4 > threshold:

                #current_detect = cowD
                #end = time.time()
                #cv2.putText(frame, "Elapsed: " + str(end - start), (200, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)

               # if (third_stack == current_detect):
                #    may_pumatong = False
                    # release ng patong
                #    sec_count = 0
                #   cv2.putText(frame, "RELEASED", (200, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)

                  #  third_stack = ""
              #  else:
                  #  if not has_drawn_already:
                    #    has_drawn_already = True
                    #    if check_pumatong(current_detect, previous_detect) is not None:
                    #        patong = check_pumatong(current_detect, previous_detect)
                    #        db_info.append(patong[0])
                    #        db_info.append(patong[1])
                    #else:
                    #    has_drawn_already = False
                   # previous_detect = cowD

           # if len(db_info) == 5:
              #  db_handler.insert_cow_overlap(db_info)
              #  sms_handler.sendSMS("Cow heat was detected: " + db_info[3] + "=>" + db_info[4])
              #  db_info = []

       # else: # No stack yet
          #  if matches > threshold:
        '''   previous_detect = cowA
                third_stack = cowA
                cv2.rectangle(frame, pointsX[curr_frame_ind], pointsY[curr_frame_ind], (0, 255, 0), 3)
                cv2.putText(frame, 'COW A FOUND', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
            elif matches2 > threshold:
                previous_detect = cowB
                third_stack = cowB
                cv2.rectangle(frame, pointsX[curr_frame_ind], pointsY[curr_frame_ind], (0, 255, 0), 3)
                cv2.putText(frame, 'COW B FOUND', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
            elif matches3 > threshold:
                previous_detect = cowC
                third_stack = cowC
                cv2.rectangle(frame, pointsX[curr_frame_ind], pointsY[curr_frame_ind], (0, 255, 0), 3)
                cv2.putText(frame, 'COW C FOUND', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
            elif matches4 > threshold:
                previous_detect = cowD
                third_stack = cowD
                cv2.rectangle(frame,pointsX[curr_frame_ind], pointsY[curr_frame_ind], (0, 255, 0), 3)
                cv2.putText(frame, 'COW D FOUND', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        '''
        cv2.imshow('Cow Heat Detection', frame)
       # if cv2.waitKey(1) == 13:  # 13 is the Enter Key
           # break

cap.release()
cv2.destroyAllWindows()