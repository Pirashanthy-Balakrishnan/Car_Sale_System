from Bean.Car import Car
from Model.OfficestaffDAO import OfficestaffDAO
from Model.StaffDAO import StaffDAO


class Staff:
    def __init__(self):

        self.staffDao = StaffDAO()

    def takemanufacturename(self):
        output = self.staffDao.manufactureNameDetails()
        manufactureNameList = []
        for m in output:
            manufactureNameList.append(m.getmanufacturename())
        return manufactureNameList

    def takeModelname(self):
        output = self.staffDao.modelNameDetails()
        modelnamelist = []
        for J in output:
            modelnamelist.append(J.get_modelname())
        return modelnamelist

    def take_Regnum(self):
        output = self.staffDao.non_SaleCar_RegNum()
        reg_Num_list = []
        for i in output:
            reg_Num_list.append(i.getRegNum())
        return reg_Num_list

    def take_ComponentName(self):
        output = self.staffDao.component_NameDetails()
        component_list = []
        for j in output:
            component_list.append(j.get_component_Name())
        return component_list

    def add_Upgrade(self, car, accessories):
        component_Name = accessories.get_component_Name()
        component_Object = self.staffDao.component_Id_Convertor(component_Name)
        component_Id_output = component_Object.get_component_id()
        # print(component_Id_output)

        component_price_Object = self.staffDao.get_Component_Price(component_Id_output)
        component_price_output = component_price_Object.get_price()

        reg_Num_output = car.getRegNum()
        upgrade_Output = self.staffDao.insert_Upgrade(component_Id=component_Id_output,
                                                      component_price=component_price_output,
                                                      reg_Num=reg_Num_output)
        return upgrade_Output










class Officestaff(Staff):
    def __init__(self):
        self.officestaffDAO = OfficestaffDAO()
        self.__output = None

        super().__init__()

    def addmanufacture(self, Manufacture):
        self.__output = self.officestaffDAO.insert_manufacture(Manufacture.getmanufacture_id(),
                                                               Manufacture.getmanufacturename())
        return self.__output

    def add_carModel(self, Carmodel, manufacture):
        #  first take get the manufacture name from the manufacture object

        # get the manufacture_id from the OfficestaffDAO model class
        results = self.officestaffDAO.get_manufactureId(manufacture.getmanufacturename())
        manufacture_id = results.get_manufacture_Id()
        # pass the model details to insert function in officestaffDAO
        insert_output = self.officestaffDAO.insertCarModel(Carmodel.get_modelid(), Carmodel.get_modelname(),
                                                           Carmodel.get_price(), manufacture_id)
        return insert_output

    def Addcardetails(self, addCar, model):
        results = self.officestaffDAO.get_modelId(model.get_modelname())
        Model_id = results.getModelid()
        insertOutput = self.officestaffDAO.insertCar(addCar.getRegNum(), addCar.getColour(),
                                                     addCar.getNumDoors(), Model_id)
        return insertOutput

    def searchCar(self, model_Name, Manufacture_Name):
        if model_Name != "" and Manufacture_Name == "" :

            result=self.officestaffDAO.fetch_SearchCar_data(model_Name)
            return result

        elif model_Name == "" and Manufacture_Name != "":
           result= self.officestaffDAO.fetch_SearchCar_data(Manufacture_Name=Manufacture_Name)
           return result
        else:
            result=self.officestaffDAO.fetch_SearchCar_data(model_Name,Manufacture_Name)
            return result

    def deleteCar(self, car):
        reg_No=car.getRegNum()
        remove_Car_detail=self.officestaffDAO.remove_Car(reg_No)
        return remove_Car_detail

    def saleCarRegnum(self):
        Sale_List=self.officestaffDAO.fetch_Sale_Detail()

        car_Reg_Num=[]
        for i in Sale_List:
            car_Reg_Num.append(i.getreg_Num())
        return car_Reg_Num

    def get_SalecarDetails(self,Reg_Num):
        Sale_List=self.officestaffDAO.fetch_Sale_Detail()
        Upgrade_List=self.staffDao.get_Car_upgrades(Reg_Num)
        sale_Car_details=[Upgrade_List]
        for j in Sale_List:
            if j.getreg_Num() == Reg_Num:
                sale_Car_details.append(j.get_final_amount())
        return sale_Car_details







