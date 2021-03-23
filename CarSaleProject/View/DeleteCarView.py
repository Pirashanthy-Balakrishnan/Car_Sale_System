from tkinter import *
from tkinter.ttk import Combobox

from Bean.Car import Car
from Logic.Staff import Officestaff
from tkinter import messagebox as mb


class DeleteCarView:
    def __init__(self):
        self.root=Tk()
        self.root.title("Delete car")
        self.root.geometry('300x200+600+300')

        self.lbl_select_Car = Label(self.root, text="selectCar")
        self.lbl_select_Car.place(x=14, y=47)

        self.combo_select_Car = Combobox(self.root, postcommand=self.selectCar)
        self.combo_select_Car.place(x=130, y=47)

        self.btn_delete = Button(self.root, text="Delete", command=self.delete)
        self.btn_delete.place(x=145, y=144)

        self.btn_back = Button(self.root, text="Back", command=self.back)
        self.btn_back.place(x=70, y=144)

        self.root.mainloop()

    def selectCar(self):
        self.combo_select_Car["values"] = Officestaff().take_Regnum()

    def delete(self):
        if self.combo_select_Car.get() == "":
            mb.showwarning("System message","Select the reg_Num in the combo box")
        else:
            select_car=self.combo_select_Car.get()
            car=Car(Reg_Num=select_car)
            output=Officestaff().deleteCar(car)

            if output:
                mb.showinfo("System message","Delete successfully")
            else:
                mb.showwarning("System message"," Not successfully deleted")


    def back(self):
        self.root.destroy()
        from View.OfficeStaffDashboardView import OfficeStaffDashboardView
        OfficeStaffDashboardView()



