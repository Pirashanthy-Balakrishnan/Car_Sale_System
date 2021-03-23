from Logic.Staff import Staff
from Model.SellerDAO import SellerDAO


class Seller(Staff):
    def __init__(self):

        self.sellerDAO=SellerDAO()
        super().__init__()


    def selected_Cardetails(self, car):
        Reg_N0=car.getRegNum()
        selectedCardetail=[]
        results=self.sellerDAO.car_details(Reg_N0)
        selectedCardetail.append(results[0].getRegNum())
        selectedCardetail.append(results[0].getColour())
        selectedCardetail.append(results[0].getNumDoors())
        selectedCardetail.append(results[1].get_modelname())
        selectedCardetail.append(results[2].getmanufacturename())

        return selectedCardetail

    def selected_Upgrade_Details(self,car):
        Reg_No=car.getRegNum()
        selected_Output=self.staffDao.get_Car_upgrades(Reg_No)
        return selected_Output

    def get_Final_price(self, car):
        car_model_Price=self.sellerDAO.get_CarModel_price(car.getRegNum())
        car_Upgrade_Price=self.sellerDAO.get_Upgrade_price(car.getRegNum())
        if car_Upgrade_Price is None:
            car_Upgrade_Price=0

        return car_model_Price + car_Upgrade_Price

    def add_new_sell(self, sale):
        output=self.sellerDAO.insert_Sale(sale.getreg_Num(),sale.get_Currency_Type(),sale.get_final_amount(),sale.get_time(),sale.get_Initial_Currency())
        return output






