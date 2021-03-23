from tkinter import *
from tkinter.ttk import Combobox


from Bean.Car import Car
from Bean.CarModel import CarModel
from Logic.Staff import Officestaff

from tkinter import messagebox as mb

from Model.LoginDAO import LoginDAO



class CarView:
    def __init__(self):
        self.root=Tk()
        self.root.title("Add_Car")
        self.root.geometry('300x280+650+350')

        self.lbl_Reg_Num = Label(self.root, text="Reg_Num")
        self.lbl_Reg_Num.place(x=14, y=47)

        self.fld_Reg_Num = Entry(self.root, width=20)
        self.fld_Reg_Num.place(x=130, y=48)

        self.lbl_Colour = Label(self.root, text="Colour")
        self.lbl_Colour.place(x=14, y=94)

        self.fld_Colour = Entry(self.root, width=20)
        self.fld_Colour.place(x=130, y=96)

        self.lbl_Num_Doors = Label(self.root, text="Num_Doors")
        self.lbl_Num_Doors.place(x=14, y=144)

        self.fld_Num_Doors = Entry(self.root, width=20)
        self.fld_Num_Doors.place(x=130, y=144)

        self.lbl_Modelname = Label(self.root, text="Modelname")
        self.lbl_Modelname.place(x=16, y=184)

        self.btn_Add = Button(self.root, text="Add", width=7, command=self.add)
        self.btn_Add.place(x=120, y=220)

        self.btn_Back = Button(self.root, text="Back", width=7, command=self.back)
        self.btn_Back.place(x=50, y=220)

        self.btn_Clear = Button(self.root, text="Clear", width=7, command=self.clear)
        self.btn_Clear.place(x=190, y=220)

        self.combo_Model_name=Combobox(self.root,postcommand=self.getModelname)
        self.combo_Model_name.place(x=130, y=184)




        self.root.mainloop()

    def getModelname(self):
        self.combo_Model_name["values"] = Officestaff().takeModelname()


    def add(self):
        if self.fld_Reg_Num.get()=="" or self.fld_Colour.get()=="" or self.fld_Num_Doors.get() =="" or self.combo_Model_name.get()=="":
           mb.showwarning("System message","Check the field and fill it")
        else:
            Reg_Num = self.fld_Reg_Num.get()
            Colour = self.fld_Colour.get()
            Num_Doors = self.fld_Num_Doors.get()
            modelname= self.combo_Model_name.get()

            car = Car(Reg_Num, Colour, Num_Doors)
            carModel=CarModel(model_name=modelname)


            outPut = Officestaff().Addcardetails(car,carModel)
            if outPut:
                mb.showinfo("Successful", "insert Succesfull")
            else:
                    mb.showwarning("Error message", "insert is not successful")

    def back(self):
        from View.OfficeStaffDashboardView import OfficeStaffDashboardView
        self.root.destroy()
        OfficeStaffDashboardView()
    def clear(self):

        self.fld_Reg_Num.delete(0, 'end')
        self.fld_Colour.delete(0, 'end')
        self. fld_Num_Doors.delete(0,'end')









