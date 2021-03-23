import sqlite3
import logging
logging.basicConfig(filename='../logging.log',filemode='w',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
class LoginDAO:

    def __init__(self):
        self.__connection=None


    # connect the database
    def getconnection(self):
        self.__connection=sqlite3.connect('../Project.db')
        return self.__connection
    # close the connect
    def close_connection(self,connect):
        if(connect):
            connect.close()


    # get the useinformation from the database
    def user_information(self):


        try:
            # call the getconnection to connect  the database
            connect=self.getconnection()
            cursor=connect.cursor()
            logging.info("connect the database successfully")

            # query for fetch the user information for user table
            query= 'select * from User'
            cursor.execute(query)
            record=cursor.fetchall()
            return record
            logging.info("successfully fetch the all data from Manufacture table")
            print(record)

        except(Exception,sqlite3.Error) as error:
            logging.error('%s error while getting data',error)


        finally:
            self.close_connection(connect)








