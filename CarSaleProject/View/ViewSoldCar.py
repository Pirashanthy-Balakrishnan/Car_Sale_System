from tkinter import *
from tkinter.ttk import Combobox

from Logic.Staff import Officestaff



class ViewSoldCar:
    def __init__(self):
        self.root=Tk()
        self.root.title("ViewSoldCar")
        self.root.geometry('350x300+600+300')

        self.lbl_select_Car = Label(self.root, text="Select car")
        self.lbl_select_Car.place(x=14, y=47)

        self.combo_select_Car = Combobox(self.root, postcommand=self.select_Car)
        self.combo_select_Car.place(x=130, y=47)

        self.lbl_Upgrade = Label(self.root, text="Upgrade")
        self.lbl_Upgrade.place(x=14, y=94)

        self.fld_Upgrade = Entry(self.root, width=20)
        self.fld_Upgrade.place(x=130, y=96)

        self.lbl_finalprice = Label(self.root, text="Finalprice")
        self.lbl_finalprice.place(x=14, y=144)

        self.fld_finalprice = Entry(self.root, width=20)
        self.fld_finalprice.place(x=130, y=144)

        self.btn_Search = Button(self.root, text="Search", width=7, command=self.Search)
        self.btn_Search.place(x=120, y=220)

        self.btn_Back = Button(self.root, text="Back", width=7, command=self.back)
        self.btn_Back.place(x=50, y=220)

        self.btn_Clear = Button(self.root, text="Clear", width=7, command=self.clear)
        self.btn_Clear.place(x=190, y=220)

        self.root.mainloop()


    def select_Car(self):

        self.combo_select_Car["values"]=Officestaff().saleCarRegnum()

    def Search(self):
        sale_Details=Officestaff().get_SalecarDetails(self.combo_select_Car.get())
        self.fld_finalprice.insert(END,sale_Details[1])


        for i in sale_Details[0]:
            self.fld_Upgrade.insert(END,i)
            self.fld_Upgrade.insert(END,",")

    def back(self):
        self.root.destroy()
        from View.OfficeStaffDashboardView import OfficeStaffDashboardView
        OfficeStaffDashboardView()

    def clear(self):
        pass



