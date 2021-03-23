from tkinter import *
from tkinter.ttk import Combobox

from Bean.Car import Car
from Logic.Seller import Seller
from Model.StaffDAO import StaffDAO
from tkinter import messagebox as mb

from View.Saleview import Saleview
from View.Upgradeview import SellerUpgrade_View


class Seller_Dashboard:
    def __init__(self):
        self.root=Tk()
        self.root.title ("selectCar")
        self.root.geometry('430x430+730+430')

        self.lbl_select_Car_RegNo = Label(self.root, text="select_Car_RegNo")
        self.lbl_select_Car_RegNo.place(x=14, y=47)

        self.combo_car_RegNo = Combobox(self.root, postcommand=self.select_Carlist)
        self.combo_car_RegNo.place(x=130, y=47)

        self.btn_view_Car = Button(self.root, text="ViewCar", command=self.ViewCar)
        self.btn_view_Car.place(x=290, y=45)

        self.lbl_Reg_No = Label(self.root, text="Reg_No")
        self.lbl_Reg_No.place(x=14, y=94)

        self.fld_Reg_No = Entry(self.root, width=20)
        self.fld_Reg_No.place(x=130, y=96)



        self.lbl_Colour = Label(self.root, text="Colour")
        self.lbl_Colour.place(x=14, y=144)

        self.fld_Colour = Entry(self.root, width=20)
        self.fld_Colour.place(x=130, y=144)

        self.lbl_Num_Doors = Label(self.root, text="Num_Doors")
        self.lbl_Num_Doors.place(x=16, y=184)

        self.fld_Num_Doors = Entry(self.root, width=20)
        self.fld_Num_Doors.place(x=130, y=184)

        self.lbl_ManufactureName = Label(self.root, text="ManufactureName")
        self.lbl_ManufactureName.place(x=20, y=222)

        self.fld_ManufactureName = Entry(self.root, width=20)
        self.fld_ManufactureName.place(x=130, y=220)

        self.lbl_Modelname = Label(self.root, text="ModelName")
        self.lbl_Modelname.place(x=32, y=252)

        self.fld_Modelname = Entry(self.root, width=20)
        self.fld_Modelname.place(x=130, y=255)



        self.btn_view_Upgrade = Button(self.root, text="ViewUpgrade", command=self.ViewUpgrade)
        self.btn_view_Upgrade.place(x=40, y=300)

        self.fld_view_Upgrade = Entry(self.root, width=15)
        self.fld_view_Upgrade.place(x=150, y=302)

        self.btn_add_newUpgrade = Button(self.root, text="newUpgrade", command=self.New_upgrade)
        self.btn_add_newUpgrade.place(x=70, y=350)

        self.btn_Sale = Button(self.root, text="Sale", command=self.Sale)
        self.btn_Sale.place(x=180,y=350)

        self.btn_Logout = Button(self.root, text="Logout", command=self.logout)
        self.btn_Logout.place(x=300, y=350)




        self.root.mainloop()

    def select_Carlist(self):
        self.combo_car_RegNo["values"] = Seller().take_Regnum()

    def ViewCar(self):
        if self.combo_car_RegNo.get() == "":
            mb.showwarning("Error","Select the Reg_Num")
        else:
            reg_Num=self.combo_car_RegNo.get()
            car=Car(reg_Num)
            car_Sale=Seller().selected_Cardetails(car)
            # print(car_Sale)
            self.fld_Reg_No.insert(END,car_Sale[0])
            self.fld_Colour.insert(END,car_Sale[1])
            self.fld_Num_Doors.insert(END,car_Sale[2])
            self.fld_Modelname.insert(END,car_Sale[3])
            self.fld_ManufactureName.insert(END,car_Sale[4])



    def ViewUpgrade(self):


        if self.combo_car_RegNo.get() == "":
            mb.showwarning("Error","Select the Reg_Num")
        else:
            reg_Num=self.combo_car_RegNo.get()
            car=Car(reg_Num)
            Upgrade_detail=Seller().selected_Upgrade_Details(car)
            for i in Upgrade_detail:
                self.fld_view_Upgrade.insert(END,i)
                self.fld_view_Upgrade.insert(END,',')





    def New_upgrade(self):
        SellerUpgrade_View()

    def Sale(self):
        car=Car(Reg_Num=self.combo_car_RegNo.get())
        final_price=Seller().get_Final_price(car)
        Saleview(car.getRegNum(),final_price)

    def logout(self):
        self.root.destroy()
        from View.LoginView import LoginView
        LoginView()

























