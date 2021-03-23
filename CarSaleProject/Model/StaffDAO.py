import sqlite3
import logging

from Bean.Accessories import Accessories
from Bean.Car import Car
from Bean.CarModel import CarModel
from Bean.Manufacture import Manufacture
from Model.LoginDAO import LoginDAO

logging.basicConfig(filename='../logging.log',filemode='w',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

class StaffDAO:
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

    def manufactureNameDetails(self):

        try:
            # call the getconnection to connect  the database
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query= 'select ManufactureName from Manufacture'
            cursor.execute(query)
            record = cursor.fetchall()

            logging.info("successfully fetching the data")
            cursor.close()
            # print(record)

            manufacturelist=[]
            for row in record:


                manufactureName=row[0]
                 # print(row[0])
                # Encapsulation manufacturename
                manufacture=Manufacture(manufacturename=manufactureName)

                manufacturelist.append(manufacture)
                # print(manufacturelist)

            return manufacturelist

        except(Exception, sqlite3.Error) as error:
            logging.error('%s error fetching data', error)

        finally:
            self.close_connection(connect)





    def modelNameDetails(self):

        try:
            # call the getconnection to connect  the database
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query= 'select Modelname from Model'
            cursor.execute(query)
            record = cursor.fetchall()

            logging.info("successfully fetching the data")
            cursor.close()
            # print(record)

            modellist=[]
            for row in record:


                modelName=row[0]
                 # print(row[0])
                # Encapsulation modelname
                carmodel=CarModel(model_name=modelName)

                modellist.append(carmodel)
                # print(modellist)

            return modellist

        except(Exception, sqlite3.Error) as error:
            logging.error('%s error fetching data', error)

        finally:
            self.close_connection(connect)


    def non_SaleCar_RegNum(self):
        try:
            # call the getconnection to connect  the database
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query= 'select Reg_Num from Car where Reg_Num not in (select Reg_Num from Sale)'
            cursor.execute(query)
            record = cursor.fetchall()

            logging.info("successfully fetching the data")
            cursor.close()

            car_List=[]
            for row in record:
                reg_Num = row[0]

                car=Car(Reg_Num=reg_Num)
                car_List.append(car)

            return car_List

        except(Exception, sqlite3.Error) as error:
            logging.error('%s error fetching reg_Num', error)

        finally:
            self.close_connection(connect)



    def component_NameDetails(self):
        try:
            # call the getconnection to connect  the database
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query= 'select ComponentName from Accessories'
            cursor.execute(query)
            record = cursor.fetchall()
            cursor.close()

            accessories_List=[]
            for row in record:
                component_Name=row[0]
                accessories=Accessories(component_Name=component_Name)
                accessories_List.append(accessories)
            return accessories_List


        except(Exception, sqlite3.Error) as error:
            logging.error('%s error fetching component_Name', error)

        finally:
            self.close_connection(connect)


    def component_Id_Convertor(self, component_Name):
        try:
            # call the getconnection to connect  the database
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query= 'select Component_id from Accessories where ComponentName = ?'

            cursor.execute(query,(component_Name,))
            record = cursor.fetchall()
            cursor.close()

            var_Component_Id=record[0][0]
            # print(component_Id)

            # Encapsulation
            accessories=Accessories(component_id=var_Component_Id)

            return accessories


        except(Exception, sqlite3.Error) as error:
            logging.error('%s error fetching component_Name', error)

        finally:
            self.close_connection(connect)


    def get_Component_Price(self, component_Id_output):

        try:
            # call the getconnection to connect  the database
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query= 'select Price from Accessories where Component_id = ?'

            cursor.execute(query, (component_Id_output,))
            record = cursor.fetchall()
            cursor.close()

            var_Component_Price=record[0][0]

            accessories=Accessories(price=var_Component_Price)

            return accessories

        except(Exception, sqlite3.Error) as error:
            logging.error('%s error fetching componentPrice', error)

        finally:
            self.close_connection(connect)


    def insert_Upgrade(self, component_Id, component_price, reg_Num):

        try:
            # call the getconnection to connect  the database
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query = "insert into Upgrade values (?,?,?)"

            cursor.execute(query, (reg_Num,component_Id,component_price))
            connect.commit()

            logging.info("successfully record is inserted")
            cursor.close()
            return True

        except(Exception, sqlite3.Error) as error:
            logging.error('%s error insert data', error)

            return False

        finally:
            self.close_connection(connect)





    def get_Car_upgrades(self, Reg_No):

        try:
            # call the getconnection to connect  the database
            connect = self.getconnection()
            cursor = connect.cursor()
            logging.info("connect the database successfully")

            query='SELECT ComponentName from Accessories WHERE Component_id in (SELECT Component_id FROM Upgrade WHERE Reg_Num = ?)'

            cursor.execute(query, (Reg_No,))
            record = cursor.fetchall()
            # print(record)

            logging.info("successfully fetching the data")
            cursor.close()

            Upgrade_list=[]
            for i in record:
                Upgrade=i[0]
                Upgrade_list.append(Upgrade)
            # print(Upgrade_list)
            return Upgrade_list

        except(Exception, sqlite3.Error) as error:
            logging.error('%s error fetching data', error)

        finally:
            self.close_connection(connect)







# StaffDAO().component_Id_Convertor('leather seats')
# StaffDAO().insert_Upgrade('A001',9000,'C002')
StaffDAO().get_Component_Price('A001')

# manufacture_list=[Manufacture(manufacture_id="m001"),
#                   Manufacture(manufacturename="shanthy"),
#                   Manufacture(manufacturename="pirasha",manufacture_id='M002'),
#                   Manufacture("M004","Balakrishnan"),
#                   Manufacture()]

