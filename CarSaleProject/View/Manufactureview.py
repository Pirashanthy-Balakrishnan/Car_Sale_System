from tkinter import *

from Bean.Manufacture import Manufacture
from Logic.Staff import Officestaff
from tkinter import messagebox as mb




class ManuFactureview:
    def __init__(self):
        self.result=None
        self.root = Tk()
        self.root.title("ManuFactureview")
        self.root.geometry('300x200+600+300')



        self.lbl_ManufactureName = Label(self.root, text="ManufactureName")
        self.lbl_ManufactureName.place(x=14, y=47)

        self.fld_ManufactureName = Entry(self.root, width=20)
        self.fld_ManufactureName.place(x=130, y=48)

        self.lbl_Manufacture_id = Label(self.root, text="Manufactureid")
        self.lbl_Manufacture_id.place(x=14, y=94)

        self.fld_Manufacture_id = Entry(self.root, width=20)
        self.fld_Manufacture_id.place(x=130, y=96)

        self.btn_Add = Button(self.root, text="Add",width=7,command=self.add)
        self.btn_Add.place(x=120,y=144)

        self.btn_Back = Button(self.root, text="Back",width=7,command=self.back)
        self.btn_Back.place(x=50,y=145)

        self.btn_Clear = Button(self.root, text="Clear",width=7,command=self.clear)
        self.btn_Clear.place(x=190, y=145)


        self.root.mainloop()


    def add(self):
        if self.fld_Manufacture_id.get() == "" or self.fld_ManufactureName.get() == "":
            mb.showwarning("System message","Check the field and fill it")
        else:
            self.manufacture=Manufacture(self.fld_Manufacture_id.get(),self.fld_ManufactureName.get())
            # manufacture=Manufacture(manufacture_id=None,manufacturename=None)
            # manufacture.setmanufacture_id(self.fld_Manufacture_id.get())
            # manufacture.setmanufacturename(self.fld_ManufactureName.get())
            # print(manufacture.getmanufacture_id())
            # self.manufacture.getmanufacture_id()
            self.result = Officestaff().addmanufacture(self.manufacture)
            if self.result:

                mb.showinfo("Successful","insert successfully")
                self.fld_ManufactureName.delete(0, 'end')
                self.fld_Manufacture_id.delete(0, 'end')

            else:
                mb.showwarning("Systemmessage","Manufacturename or Manufacture_id already exist")

    def back(self):
        from View.OfficeStaffDashboardView import OfficeStaffDashboardView
        self.root.destroy()
        OfficeStaffDashboardView()

    def clear(self):
        self.fld_ManufactureName.delete(0, 'end')
        self.fld_Manufacture_id.delete(0, 'end')











