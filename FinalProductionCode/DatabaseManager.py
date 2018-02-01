import MySQLdb # Database connector

class DBManager():

    #Here we initialize the database...
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",
                                  user="root",
                                  passwd="",
                                  db="etrus")
        self.cursor = self.db.cursor()


    ### Use Tuples as parameter
    def insert_cow_tracking(self,data):
        self.cursor.execute("INSERT INTO tbl_cow_track (cow_number,cow_track_timestamp,cow_track_timestamp) VALUES (?,?,?)",data['cow_num'],data['cow_time']);

    def insert_cow_overlap(self,data):
        print(len(data))
        print(data)
        result = self.cursor.execute("INSERT INTO tbl_cow_detected (time,date,num_sec,cow_id,stats,cow_partner_id) VALUES (%s,%s,%s,%s,%s,%s)",(data[0],data[1],data[2],data[3],"cow",data[4]))
        self.db.commit()
        print(result)

    def insert_cow_position(self,sector,streamname,framecount,featurecount,cowname):

        print "Logging: "
        print sector #
        print streamname
        print framecount #
        print featurecount #
        print cowname#

        result = self.cursor.execute("INSERT INTO tbl_cow_track (cow_track_sector,cow_stream,cow_frame_number,cow_feature_count,cow_name) VALUES (%s,%s,%i,%i,%s)")

        self.db.commit();

        print(result)



