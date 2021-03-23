from tkinter import *
from tkinter.ttk import Combobox
import abc

from Bean.Accessories import Accessories
from Bean.Car import Car
from Logic.Staff import Officestaff
from tkinter import messagebox as mb
from Model.StaffDAO import StaffDAO



class Upgadeview(abc.ABC):
    def __init__(self):
        self.root = Tk()
        self.root.title("Upgradeview")
        self.root.geometry('300x200+600+300')

        self.lbl_Reg_Num = Label(self.root, text="Reg_Num")
        self.lbl_Reg_Num.place(x=14, y=47)

        self.combo_Reg_Num = Combobox(self.root, postcommand=self.reg_Numlist)
        self.combo_Reg_Num.place(x=130, y=48)

        self.lbl_Component_name = Label(self.root, text="Component_name")
        self.lbl_Component_name.place(x=14, y=94)

        self.combo_componentName = Combobox(self.root, postcommand=self.component_List)
        self.combo_componentName.place(x=130, y=96)

        self.btn_submit = Button(self.root, text="Submit", command=self.submit)
        self.btn_submit.place(x=125, y=144)

        self.btn_back = Button(self.root, text="Back", command=self.back)
        self.btn_back.place(x=30, y=144)

        self.btn_clear = Button(self.root, text="Clear", command=self.clear)
        self.btn_clear.place(x=220, y=144)

        self.root.mainloop()

    def reg_Numlist(self):
        self.combo_Reg_Num["values"] = Officestaff().take_Regnum()

    def component_List(self):
        self.combo_componentName["values"] = Officestaff().take_ComponentName()

    def submit(self):
        if self.combo_Reg_Num.get() == "" or self.combo_componentName.get()=="":
            mb.showwarning("System message","Check the field and fill it")
        else:
            reg_Num = self.combo_Reg_Num.get()
            component_name = self.combo_componentName.get()
            car = Car(reg_Num)
            accessories = Accessories(component_Name=component_name)
            results = Officestaff().add_Upgrade(car, accessories)
            if results:
                mb.showinfo("Successful", "insert Sccessful")
            else:
                mb.showwarning("Error message", "insert not successful")

    @abc.abstractmethod
    def back(self):
        pass

    def clear(self):
        self.combo_componentName.delete(0, END)
        self.combo_Reg_Num.delete(0, END)


class Officestaff_Upgrade_View(Upgadeview):

    def back(self):
        self.root.destroy()
        from View.OfficeStaffDashboardView import OfficeStaffDashboardView
        OfficeStaffDashboardView()



class SellerUpgrade_View(Upgadeview):
    def back(self):
        self.root.destroy()










