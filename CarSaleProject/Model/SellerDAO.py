import logging
import sqlite3

from Bean.Car import Car
from Bean.CarModel import CarModel
from Bean.Manufacture import Manufacture

logging.basicConfig(filename='../logging.log', filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
class SellerDAO:
    def __init__(self):
        self.__connection = None

    def getconnection(self):
        self.__connection = sqlite3.connect('../Project.db')
        return self.__connection

        # close the connection

    def close_connection(self, connect):
        if (connect):
            connect.close()
            logging.info("connection is closed")

    def car_details(self, Reg_N0):
        try:
            # call the getconnection to connect  the database
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query= 'select Reg_Num,Colour,NumOfDoors,Modelname,ManufactureName from Car,Model,Manufacture where Model.Manudacture_id = Manufacture.Manufacture_id and Model.Model_id =Car.Model_id and Car.Reg_Num =?'

            cursor.execute(query,(Reg_N0,))
            record = cursor.fetchall()
            # print(record)

            logging.info("successfully fetching the data")
            cursor.close()

            car=Car(record[0][0],record[0][1],record[0][2])
            carmodel=CarModel(model_name=record[0][3])
            manufacture=Manufacture(manufacturename=record[0][4])

            car_detalis_list=[car,carmodel,manufacture]
            return car_detalis_list



        except(Exception, sqlite3.Error) as error:
            logging.error('%s error fetching data', error)

        finally:
            self.close_connection(connect)
    #
    # def get_Car_upgrades(self, Reg_No):
    #
    #     try:
    #         # call the getconnection to connect  the database
    #         connect = self.getconnection()
    #         cursor = connect.cursor()
    #         logging.info("connect the database successfully")
    #
    #         query='SELECT ComponentName from Accessories WHERE Component_id in (SELECT Component_id FROM Upgrade WHERE Reg_Num = ?)'
    #
    #         cursor.execute(query, (Reg_No,))
    #         record = cursor.fetchall()
    #         # print(record)
    #
    #         logging.info("successfully fetching the data")
    #         cursor.close()
    #
    #         Upgrade_list=[]
    #         for i in record:
    #             Upgrade=i[0]
    #             Upgrade_list.append(Upgrade)
    #         # print(Upgrade_list)
    #         return Upgrade_list
    #
    #     except(Exception, sqlite3.Error) as error:
    #         logging.error('%s error fetching data', error)
    #
    #     finally:
    #         self.close_connection(connect)

    def get_CarModel_price(self, Reg_No):
        try:
            # call the getconnection to connect  the database
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query='SELECT Price FROM Model WHERE Model_id in (SELECT Model_id FROM Car WHERE Reg_Num = ?)'

            cursor.execute(query, (Reg_No,))
            price = cursor.fetchall()

            return price[0][0]

        except(Exception, sqlite3.Error) as error:
            logging.error('%s error fetching data', error)

        finally:
            self.close_connection(connect)

    def get_Upgrade_price(self, Reg_No):
        try:
            # call the getconnection to connect  the database
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query = 'SELECT sum(Final_Price) from Upgrade WHERE Reg_Num = ?'

            cursor.execute(query, (Reg_No,))
            price = cursor.fetchall()

            return price[0][0]

        except(Exception, sqlite3.Error) as error:
            logging.error('%s error fetching data', error)

        finally:
            self.close_connection(connect)

    def insert_Sale(self,Reg_Num,currency_Type,final_Amount, time, Inital_currency):
        try:
            # call the getconnection to connect  the database
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query = 'INSERT INTO Sale (Reg_Num,Currency_Type,Finalamount,time_Stamp,Initial_Currency) VALUES (?,?,?,?,?) '

            cursor.execute(query, (Reg_Num,currency_Type,final_Amount,time,Inital_currency))
            connect.commit()

            logging.info("successfully record is inserted")
            cursor.close()

            return True


        except(Exception, sqlite3.Error) as error:
            logging.error('%s error insert data', error)

            return False

        finally:
            self.close_connection(connect)

# print(SellerDAO().get_CarModel_price("C001"))

