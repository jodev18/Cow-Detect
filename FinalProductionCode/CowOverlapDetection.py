import numpy as np
import cv2
import time
import requests
from SmsManager import SMSSender
from DatabaseManager import DBManager
from datetime import datetime
import threading
from threading import Thread, Event, ThreadError
from serial import SerialException
from os import listdir
from os.path import isfile, join



class Cam():

  def __init__(self, url,frame_name):
    
    self.stream = requests.get(url, stream=True)
    self.thread_cancelled = False
    self.thread = Thread(target=self.run)
    self.frame_id = frame_name
    print "camera initialised"

    self.imagemodels = []
    self.modelpath = "cow_models"

    print "Loading image models..."

    self.matchlist = []
    self.filelist = [f for f in listdir(self.modelpath) if isfile(join(self.modelpath, f))]

    #dynamically load image models based on file folder contents
    if len(self.filelist) > 0:
        print "--------------"
        print "Loading " +  str(len(self.filelist)) + " image models..."
        for file in self.filelist:
            print "Added " + file + " to list of models."
            self.imagemodels.append((file,cv2.imread(self.modelpath + file,0)))

    # Load our image template, this is our reference image
    self.image_template = cv2.imread('../imagemodels/rmodels/COW_A.jpg', 0)
    self.image_template2 = cv2.imread('../imagemodels/rmodels/COW_B.jpg', 0)
    self.image_template3 = cv2.imread('../imagemodels/rmodels/COW_C.jpg', 0)
    self.image_template4 = cv2.imread('../imagemodels/rmodels/COW_D.jpg', 0)
    print "image template initialized."

    # Our threshold to indicate object deteciton
    # We use 10 since the SIFT detector returns little false positves
    self.threshold = 10

    self.classifier = cv2.CascadeClassifier('cascades/haarcascade_fullbody.xml');

    print "Threshold value: " + str(self.threshold)

    self.current_frame = None
    self.current_template = None

    # For the SMS and database stuff..
    #self.sms_handler = SMSSender()
    self.db_handler = DBManager()

    print "Database initialized."

    self.cowA = "COW A"
    self.cowB = "COW B"
    self.cowC = "COW C"
    self.cowD = "COW D"

    self.previous_detect = ''
    self.current_detect = ''
    self.third_stack = ''

    self.sec_count = 0

    self.may_pumatong = False
    self.has_drawn_already = False


  def start(self):
    self.thread.start()
    print "camera stream started"

  def sift_detector(self,frame,template):

    if frame is not None and template is not None:

        image1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # change to grayscale
        #image2 = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        # Create SIFT detector object
        sift = cv2.SIFT(180)  # limit to 180 features for permLfomance

        # Obtain the keypoints and descriptors using SIFT
        keypoints_1, descriptors_1 = sift.detectAndCompute(image1, None)
        keypoints_2, descriptors_2 = sift.detectAndCompute(template, None)

        #print(image1)
        #print(template)

        # Define parameters for our Flann Matcher
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=3)
        search_params = dict(checks=100)

        # Create the Flann Matcher object
        flann = cv2.FlannBasedMatcher(index_params, search_params)

        # Obtain matches using K-Nearest Neighbor Method
        # the result 'matches' is the number of similar matches found in both images
        matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

        # Store good matches using Lowe's ratio test
        good_matches = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good_matches.append(m)

        return len(good_matches)
    else:
        print "Frame none"
        return 0

  def run(self):

    bytes=''
    frame_count = 0
    curr_date = datetime.now().date()
    curr_time = datetime.now().time()
    start = time.time()

    while not self.thread_cancelled:
      try:
        sec_trigger = frame_count % 30
        bytes+=self.stream.raw.read(1024)
        a = bytes.find('\xff\xd8')
        b = bytes.find('\xff\xd9')
        if a!=-1 and b!=-1:
          frame_count = frame_count + 1
          curr_frame_ind = frame_count % 6
          #sec_trigger = frame_count % 30

          jpg = bytes[a:b+2]
          bytes= bytes[b+2:]
          frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)

          if frame is not None:
              height, width = frame.shape[:2]

              # Define ROI Box Dimensions
              top_left_x = 0  # width / 3
              top_left_y = 0  # (height / 2) + (height / 4)
              bottom_right_x = (width / 3)
              bottom_right_y = (height / 2)

              # Draw rectangular window for our region of interest
              pointsX = [(top_left_x, top_left_y), (bottom_right_x, top_left_y), (bottom_right_x * 2, top_left_y),
                         (top_left_x, bottom_right_y), (bottom_right_x, bottom_right_y),
                         (bottom_right_x * 2, bottom_right_y)]
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

              #frame = cv2.flip(frame, 1)

              #draw cascade over detected areas
              grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

              # Pass frame to our car classifier
              cars = self.classifier.detectMultiScale(grayframe, 1.4, 2)

              for (x, y, w, h) in cars:
                  cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

              for (filenamae,model) in self.imagemodels:
                  match_res = self.sift_detector(cropped,model)

                  if match_res > 0:
                      self.matchlist.append((filenamae,match_res))

              for (fname,mdata) in self.matchlist:
                  print fname + ":"
                  print mdata
              # Get number of SIFT matches
              #matches = self.sift_detector(cropped,self.image_template)
              #matches2 = self.sift_detector(cropped, self.image_template2)
              #matches3 = self.sift_detector(cropped, self.image_template3)
              #matches4 = self.sift_detector(cropped, self.image_template4)

              #print ("First M Match:" + str(matches))
              #print ("Second M Match:" + str(matches2))
              #print ("Third M Match:" + str(matches3))
              #print ("Fourth M Match:" + str(matches4))

              #cv2.putText(frame, str(matches), (450, 450), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 1)

              # If matches exceed our threshold then object has been detected
              # if not previous_detect is None:

              may_pumatong = True

              db_info = []
              db_info.append(str(curr_time))
              db_info.append(str(curr_date))
              db_info.append(str('5:00'))


              if(sec_trigger == 0):
                self.sec_count = self.sec_count + 1
                cv2.putText(frame,"Sec: " + str(self.sec_count),(200,450), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),1)



              if len(db_info) == 5:
                 print('saving to database')
                 self.db_handler.insert_cow_overlap(db_info)

                 try:
                     sms_handler = SMSSender()
                    #sms_handler.sendSMS('9486598145', "Cow heat was detected: " + db_info[3] + "=>" + db_info[4])
                 except SerialException:
                     print("Serial port was occupied")
                 finally:
                     db_info = []

              else:
                  print(self.frame_id + ': No stacking yet')

              cv2.imshow(self.frame_id, frame)
              cv2.imwrite('temp_run_img.jpg', frame) # continuously overwrites the file
              cv2.imshow(self.frame_id + " Current Frame",cropped)

              if cv2.waitKey(1) ==27:
               exit(0)
          else:
              print "Video frame is none!"
        else:
            print "Some gaps in the video stream..."

      except ThreadError:
        print('Thread error for ' + self.frame_id)
        self.thread_cancelled = True
        cv2.destroyWindow(self.frame_id)

  def is_running(self):
    return self.thread.isAlive()
      
    
  def shut_down(self):
    self.thread_cancelled = True
    #block while waiting for thread to terminate
    while self.thread.isAlive():
      time.sleep(1)
    return True

  def check_pumatong(self,frame,pumatong, pinatungan, point1, point2):

    if pumatong != pinatungan:
      patong_info = []
      cv2.rectangle(frame, point1, point2, (0, 255, 0), 3)
      cv2.putText(frame, pumatong + " and " + pinatungan + " are in-heat.", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1,
                  (0, 255, 0), 1)
      patong_info.append(pumatong)
      patong_info.append(pinatungan)
      print(pumatong + "=>" + pinatungan)
      return patong_info
    else:
      return None

  def detect_cow(self,framename,cowname,coordX,coordY):
      self.previous_detect = cowname
      self.third_stack = cowname
      cv2.rectangle(framename, coordX,coordY, (0, 255, 0), 3)
      cv2.putText(framename, cowname + ' found.', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)

  def detect_and_check_overlap(self,image,imagetemplate):

      match_info = self.sift_detector(image,imagetemplate)

      if match_info > self.threshold:
          print "Huh"
      else:
          print "Ok"


  def start_scan(self,streamlink,windowtitle):
      # smsbroker = SMSSender()
      print "========COW OVERLAP DETECTION========"
      try:
          # # 'samplevids/sample3.mp4''http://192.168.1.7:8080/video'
          print "-----------------------------------"
          if len(streamlink) > 0:
              if len(windowtitle) > 0:
                  print "Stream Link: " + streamlink
                  print "Window title set: " + windowtitle
                  print "Starting stream and processing..."
                  cam = Cam(streamlink, windowtitle)
                  cam.start()
              else:
                  print "Window title must not be empty."
          else:
              print "Stream link must not be empty."
      except Exception as ex:
          template = "An exception of type {0} occurred. Arguments:\n{1!r}"
          message = template.format(type(ex).__name__, ex.args)
          print message

      print "-----------------------------------"

  #url2 = 'http://127.0.0.1:8888/mjpg/002'
  #cam2 = Cam(url2,'CAMERA 2')
  #cam2.start()
  #url3 = 'http://127.0.0.1:8888/mjpg/002'
  #cam3 = Cam(url2, 'CAMERA 2')
  #cam3.start()
  #url4 = 'http://127.0.0.1:8888/mjpg/002'
  #cam4 = Cam(url2, 'CAMERA 2')
  #cam4.start()