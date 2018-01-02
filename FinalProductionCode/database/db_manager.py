
import mysql.connector
from mysql.connector import errorcode

class MySQLHelper:

    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user='root',
                                          database='etrus')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def login(self,username,password):
        self.cursor = self.cnx.cursor()
        query = ("SELECT count(username) from tbl_login_users WHERE username=%s AND password=%s",(username,password))

        self.cursor.execute(query)

        #print self.cursor
        #for cc in self.cursor:
           # print cc

    def closeDB(self):
        self.cnx.close()