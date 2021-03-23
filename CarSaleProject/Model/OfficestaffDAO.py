import sqlite3
import logging

from Bean.Car import Car
from Bean.CarModel import CarModel
from Bean.Manufacture import Manufacture
from Bean.Sale import Sale

logging.basicConfig(filename='../logging.log',filemode='w',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)


class OfficestaffDAO:
    def __init__(self):
        self.__connection=None

    def getconnection(self):
        self.__connection=sqlite3.connect('../Project.db')
        return self.__connection

    # close the connection
    def close_connection(self, connect):
        if(connect):
            connect.close()
            logging.info("connection is closed")



    def insert_manufacture(self,Manufacture_id,Manufacturename):


        try:
            # call the getconnection to connect  the database
            connect=self.getconnection()
            cursor=connect.cursor()
            logging.info("connect the database successfully")



            query = "insert into Manufacture values (?,?)"

            cursor.execute(query,(Manufacture_id,Manufacturename))
            connect.commit()

            logging.info("successfully record is inserted")
            cursor.close()
            return True

        except(Exception, sqlite3.Error) as error:
            logging.error('%s error insert data', error)
            return False

        finally:
            self.close_connection(connect)


    def get_manufactureId(self,manufactureName):
        try:
            # call the getconnection to connect  the database
            connect=self.getconnection()
            cursor=connect.cursor()
            logging.info("connect the database successfully")

            query = "select Manufacture_id from Manufacture where ManufactureName = ?"

            cursor.execute(query,(manufactureName,))
            record=cursor.fetchall()



            logging.info("successfully fetch the manufactureid")
            cursor.close()
            # manufactureid = record[0][0]
            for i in record:
                # print(i[0])
                manufactureid=i[0]
                # print(manufactureid)
            #     manufacture=Manufacture(manufacture_id=manufactureid)
                car_Model=CarModel(manufacture_id=manufactureid)

            return car_Model

        except(Exception, sqlite3.Error) as error:
            logging.error('%s error fetching data', error)

        finally:
            self.close_connection(connect)



    def insertCarModel(self, model_Id, model_Name, price, manufacture_Id):

        try:
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query = "insert into Model values (?,?,?,?)"

            cursor.execute(query, (model_Id, model_Name, price, manufacture_Id))
            connect.commit()

            logging.info("successfully record is inserted")
            cursor.close()

            return True

        except(Exception, sqlite3.Error) as error:
            logging.error('%s error insert data', error)

            return False

        finally:
            self.close_connection(connect)



    def get_modelId(self, modelName):
        try:
            # call the getconnection to connect  the database
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query = "select Model_id from Model where Modelname = ?"

            cursor.execute(query, (modelName,))
            record = cursor.fetchall()

            logging.info("successfully fetch the Model_id")
            cursor.close()
            # Model_id = record[0][0]
            for i in record:
                # print(i[0])
                Modelid = i[0]
                # print(Modelid)

                add_Car = Car(Model_id=Modelid)

            return add_Car

        except(Exception, sqlite3.Error) as error:
            logging.error('%s error fetching data', error)

        finally:
            self.close_connection(connect)




    def insertCar(self,Reg_Num, Colour, Num_Doors, Model_id):

        try:
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query = "insert into Car values (?,?,?,?)"

            cursor.execute(query, (Reg_Num, Colour, Num_Doors, Model_id))
            connect.commit()

            logging.info("successfully record is inserted")
            cursor.close()

            return True

        except(Exception, sqlite3.Error) as error:
            logging.error('%s error insert data', error)

            return False

        finally:
            self.close_connection(connect)

    def fetch_SearchCar_data(self, model_Name=None, Manufacture_Name=None):
        try:
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")


            if model_Name is not  None and Manufacture_Name is None :
                # Get the car details are taken under the car model
                query='SELECT * FROM Car WHERE Model_id in (SELECT Model_id FROM Model WHERE Modelname = ?)'

                cursor.execute(query, (model_Name,))
                record=cursor.fetchall()

            elif model_Name is None and Manufacture_Name is not None:
                # Get the car details are taken under the Manufacture
                query = 'SELECT * FROM Car WHERE car.Model_id in (SELECT Model.Model_id FROM Model WHERE Model.Manudacture_id in (SELECT Manufacture.Manufacture_id FROM Manufacture WHERE ManufactureName = ?))'

                cursor.execute(query, (Manufacture_Name,))
                record = cursor.fetchall()

            else:
                # Get the car details are taken under the Model and Manufacture
                query = 'SELECT * from Car where Model_id in (SELECT Model_id FROM model WHERE Modelname = ? )or Model_id in (SELECT Model_id FROM Model WHERE Model.Manudacture_id in (SELECT Manufacture.Manufacture_id FROM Manufacture WHERE ManufactureName=?))'

                cursor.execute(query, (model_Name,Manufacture_Name,))
                record = cursor.fetchall()

        except(Exception, sqlite3.Error) as error:
            logging.error('%s error insert data', error)

            return False

        else:
            cursor.close()
            return record

        finally:
            self.close_connection(connect)

    def remove_Car(self, reg_No):
        try:
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query='DELETE FROM Car where Reg_Num = ?'

            cursor.execute(query,(reg_No,))
            connect.commit()
            cursor.close()

            return True

        except(Exception, sqlite3.Error) as error:
            logging.error('%s error insert data', error)

            return False
        finally:
            self.close_connection(connect)

    def fetch_Sale_Detail(self):

        try:
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query='select Sale.Reg_Num,Finalamount FROM Sale'

            cursor.execute(query)
            record = cursor.fetchall()

            logging.info("successfully fetch the Reg_Num")
            cursor.close()

            sale_List=[]
            for row in record:
                car_RegNum=row[0]
                final_Amount=row[1]

                sale=Sale(Reg_Num=car_RegNum,Finalamount=final_Amount)
                sale_List.append(sale)
            return sale_List

        except(Exception, sqlite3.Error) as error:
            logging.error('%s error insert data', error)


        finally:
            self.close_connection(connect)







# print(OfficestaffDAO().fetch_SearchCar_data("duck","Admos"))














