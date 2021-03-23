from tkinter import *
from tkinter.ttk import Combobox


from Bean.CarModel import CarModel
from Bean.Manufacture import Manufacture
from Logic.Staff import Officestaff
from tkinter import messagebox as mb


class CarmodelView:
    def __init__(self):
        self.root=Tk()
        self.root.title("model view")
        self.root.geometry('300x280+650+350')

        self.lbl_Model_id = Label(self.root, text="Model_id")
        self.lbl_Model_id.place(x=14, y=47)

        self.fld_Model_id = Entry(self.root, width=20)
        self.fld_Model_id.place(x=130, y=48)


        self.lbl_Modelname = Label(self.root, text="Modelname")
        self.lbl_Modelname.place(x=14, y=94)

        self.fld_Modelname = Entry(self.root, width=20)
        self.fld_Modelname.place(x=130, y=96)

        self.lbl_Price = Label(self.root, text="price")
        self.lbl_Price.place(x=14, y=144)

        self.fld_price = Entry(self.root, width=20)
        self.fld_price.place(x=130, y=144)

        self.lbl_Manufacturename = Label(self.root, text="Manufacturename")
        self.lbl_Manufacturename.place(x=16, y=184)

        self.btn_Add = Button(self.root, text="Add", width=7, command=self.add)
        self.btn_Add.place(x=120, y=220)

        self.btn_Back = Button(self.root, text="Back", width=7, command=self.back)
        self.btn_Back.place(x=50, y=220)

        self.btn_Clear = Button(self.root, text="Clear", width=7, command=self.clear)
        self.btn_Clear.place(x=190, y=220)




        self.combo_Manufacturename = Combobox(self.root, postcommand=self.getManufacturename)

        self.combo_Manufacturename.place(x=130, y=184)
        # self.Manufacturename.current(1)
        self.root.mainloop()


    def getManufacturename(self):
        self.combo_Manufacturename["values"]=Officestaff().takemanufacturename()

    def add(self):
        if self.fld_Model_id.get()=="" or self.fld_Modelname.get()=="" or self.fld_price.get() =="" or self.combo_Manufacturename.get()=="":
            mb.showwarning("System message","Check the field and fill it")
        else:

            model_Id=self.fld_Model_id.get()
            model_Name=self.fld_Modelname.get()
            model_price=self.fld_price.get()
            manufacture_Name=self.combo_Manufacturename.get()

            carModel = CarModel(model_Id, model_Name, model_price)
            manufacture=Manufacture(manufacturename=manufacture_Name)

            outPut=Officestaff().add_carModel(carModel,manufacture)
            if outPut:
                mb.showinfo("Successful","insert Succesfull")
            else:
                mb.showwarning("Error message","insert is not successful")

    def back(self):
        from View.OfficeStaffDashboardView import OfficeStaffDashboardView
        self.root.destroy()
        OfficeStaffDashboardView()
    def clear(self):

        self.fld_Model_id.delete(0, 'end')
        self.fld_Modelname.delete(0, 'end')
        self. fld_price.delete(0,'end')










