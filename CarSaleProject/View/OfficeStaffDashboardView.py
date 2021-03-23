from tkinter import *

from View.CarView import CarView
from View.CarmodelView import CarmodelView
from View.DeleteCarView import DeleteCarView
from View.Manufactureview import ManuFactureview
from View.SearchCarView import SearchCarView
from View.Upgradeview import Upgadeview, Officestaff_Upgrade_View
from View.ViewSoldCar import ViewSoldCar


class OfficeStaffDashboardView:

    # Create office staff UI
    def __init__(self):
        self.window = Tk()
        self.window.title("Office Staff Dashboard")
        self.window.geometry('350x200+600+300')

        # create the office staff dashboard button
        self.btn_AddManufacture = Button(self.window, text="Add manufacture", width=18,
                                         command=lambda: self.clickDashboard('btn_AddManufacture'))
        self.btn_AddManufacture.place(x=10, y=10)

        # create the  add car dashboard
        self.btn_AddCar = Button(self.window, text="Add car", width=18,
                                 command=lambda: self.clickDashboard('btn_AddCar'))
        self.btn_AddCar.place(x=10, y=50)

        # create delete dashboard
        self.btn_DeleteCar = Button(self.window, text="Delete car", width=18,
                                    command=lambda: self.clickDashboard('btn_DeleteCar'))
        self.btn_DeleteCar.place(x=10, y=90)

        # create view sold car
        self.btn_ViewSoldCar = Button(self.window, text="View sold car", width=18,
                                      command=lambda: self.clickDashboard('btn_ViewSoldCar'))
        self.btn_ViewSoldCar.place(x=10, y=140)

        # create add model
        self.btn_AddModel = Button(self.window, text="Add model", width=18,
                                   command=lambda: self.clickDashboard('btn_AddModel'))
        self.btn_AddModel.place(x=170, y=10)

        # create add upgrade
        self.btn_AddUpgrade = Button(self.window, text="Add upgrade", width=18,
                                     command=lambda: self.clickDashboard('btn_AddUpgrade'))
        self.btn_AddUpgrade.place(x=170, y=50)

        # create search car
        self.btn_SearchCar = Button(self.window, text="Search car", width=18,
                                    command=lambda: self.clickDashboard('btn_SearchCar'))

        self.btn_SearchCar.place(x=170, y=90)

        # create logout
        self._btnLogout = Button(self.window, text="Logout", width=18,
                                 command=lambda: self.clickDashboard('btn_Logout'))
        self._btnLogout.place(x=170, y=140)

        self.window.mainloop()

    def clickDashboard(self, buttonName):
        # Check the button name and open the particular window

        if buttonName == 'btn_AddManufacture':
            # Close the office staff dashboard
            # Open the manufacture view
            self.window.destroy()
            ManuFactureview()

        elif buttonName == 'btn_AddCar':
            self.window.destroy()
            CarView()

        elif buttonName == 'btn_DeleteCar':
            self.window.destroy()
            DeleteCarView()

        elif buttonName == 'btn_ViewSoldCar':
           self.window.destroy()
           ViewSoldCar()

        elif buttonName == 'btn_AddModel':
            self.window.destroy()
            CarmodelView()

        elif buttonName == 'btn_AddUpgrade':
            self.window.destroy()
            Officestaff_Upgrade_View()

        elif buttonName == 'btn_SearchCar':
            self.window.destroy()
            SearchCarView()

        elif buttonName == 'btn_Logout':
           self.window.destroy()
           from View.LoginView import LoginView
           LoginView()
