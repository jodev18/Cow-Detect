import cv2
import collections
from os import listdir
from os.path import isfile, join
from DatabaseManager import DBManager

class SeeCows():

    def main(self):
        print("Initialized cow detector")
        self.init_scan()

    def __init__(self):
        self.db = DBManager()
        #Open the files we wish to show
        self.cap = cv2.VideoCapture('images/sample1.avi')
        self.cap2 = cv2.VideoCapture('images/sample2.avi')
        self.cap3 = cv2.VideoCapture('images/sample3.avi')
        self.cap4 = cv2.VideoCapture('images/sample4.avi')

        self.frame_count = 0

        # Confidence for detecting cow path
        self.MIN_CONFIDENCE = 4

        ### GETS ALL IMAGES from COW_REFERENCES FOLDER AND USES IT AS TEMPLATE ###
        self.mypath = 'images/cow_references/'

        self.onlyfiles = [f for f in listdir(self.mypath) if isfile(join(self.mypath, f))]

        if (len(self.onlyfiles) > 0):
            templs = []
            for fil in self.onlyfiles:
                templs.append(cv2.imread('images/cow_references/' + fil, 0))

            self.the_temps = templs

        self.cow_path = []  # Container for the sectors the cow has traversed.

    def sift_detector(self,new_image, image_template):
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

    def comparetemps(self,tempps, orig_feed, index):
        mx_data = self.sift_detector(orig_feed, tempps)

        threshold = 15

        if mx_data >= threshold:
            return self.onlyfiles[index]
        else:
            return None

    def init_scan(self):
        while True:

            # To check for the frame count...
            self.frame_count = self.frame_count + 1

            self.curr_frame_ind = self.frame_count % 6

            # Get webcam images
            ret, frame = self.cap.read()
            ret2, fr2 = self.cap2.read()
            ret3, frame3 = self.cap3.read()
            ret4, frame4 = self.cap4.read()

            self.frame = cv2.pyrDown(frame)
            self.fr2 = cv2.pyrDown(fr2)
            self.frame3 = cv2.pyrDown(frame3)
            self.frame4 = cv2.pyrDown(frame4)

            self.frame2 = frame.copy()

            self.curr_frames = [self.frame,self.frame2,self.fr2,self.frame3,self.frame4]
            self.frame_labels = [ 'Cow Detection A', 'Cow Detection B', 'Cow Detection C', 'Cow Detection D']

            # Get height and width of webcam frame
            self.scan_frame(self.curr_frames[0], self.frame_labels[0])

            # thread.start_new_thread(scan_frame,(frame,'Cow Detection A'))
            # thread.start_new_thread(scan_frame,(fr2,'Cow Detection B'))
            # thread.start_new_thread(scan_frame,(frame3,'Cow Detection C'))
            # thread.start_new_thread(scan_frame,(frame4,'Cow Detection D'))

            if cv2.waitKey(1) == 13:  # 13 is the Enter Key
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def scan_frame(self,frame,windowTitle):

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
        cv2.rectangle(frame, pointsX[self.curr_frame_ind], pointsY[self.curr_frame_ind], 255, 3)

        ### WE CROP THE FRAME INTO 6 PARTS, TO IMPROVE EFFICIENCY OF DETECTION ##

        cropped1 = frame[top_left_x:bottom_right_y, top_left_y:bottom_right_x]
        cropped2 = frame[top_left_x:bottom_right_y, bottom_right_x:bottom_right_x * 2]
        cropped3 = frame[top_left_x:bottom_right_y, bottom_right_x * 2:bottom_right_x * 3]

        cropped4 = frame[bottom_right_y:bottom_right_y * 2, top_left_x:bottom_right_x]
        cropped5 = frame[bottom_right_y:bottom_right_y * 2, bottom_right_x:bottom_right_x * 2]
        cropped6 = frame[bottom_right_y:bottom_right_y * 2, bottom_right_x * 2:bottom_right_x * 3]

        crops = [cropped1, cropped2, cropped3, cropped4, cropped5, cropped6]

        cropped = crops[self.curr_frame_ind]

        txt_x, txt_y = pointsX[self.curr_frame_ind]

        cv2.putText(self.frame2, 'Scanning...', (txt_x, txt_y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        index = 0

        detectedlist = []

        for temp in self.the_temps:
            result = self.comparetemps(temp, cropped, index)
            index = index + 1

            if not result is None:
                detectedlist.append(result)

        if (len(detectedlist) > 0):
            has_detected = True

            cow_names = []

            cv2.putText(frame, 'Detected:', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            for item in detectedlist:
                cv2.rectangle(frame, pointsX[self.curr_frame_ind], pointsY[self.curr_frame_ind], (0, 255, 0), 3)
                cow_names.append(item[:4])

            counter = collections.Counter(cow_names)

            cow_count = counter.values()
            cow_n = counter.keys()

            cnc = 0  # cow name counter, for iterating through the cow counts

            linebreak = 8

            for cn in cow_n:
                cv2.putText(frame, cn + ":" + str(cow_count[cnc]), (10, 20 + 20 + linebreak), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,
                            (0, 255, 0), 2)
                cnc = cnc + 1
                linebreak = linebreak + 10

            if not cow_count is None:
                if not cow_n is None:
                    print(cow_count)
                    print(cow_n)
                    self.cow_path.append([(self.curr_frame_ind, self.frame_count), (cow_count, cow_n)])

                print ("COW PATH")
                print (self.cow_path)
                # print (cow_path[curr_frame_ind])

                    # analyzedPath = PathAnalyzer(cow_path)
        else:
            has_detected = False

        if has_detected:
            cv2.imshow(self.frame_labels[0], frame)
        else:
            cv2.imshow(self.frame_labels[1], self.frame2)

    if __name__ == '__main__':
        main()