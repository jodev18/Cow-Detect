
import mysql.connector

class MySQLHelper():

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='etrus')
