from tkinter import *
from tkinter import messagebox as mb

from Bean.User import User
from Logic.Logiccontroller import LoginController
from View.OfficeStaffDashboardView import OfficeStaffDashboardView
from View.seller_Dashboard import Seller_Dashboard


class LoginView:
    # Create a login UI
    def __init__(self):
        self.root = Tk()
        self.root.title("Login")
        self.root.geometry('300x200+600+300')

        self.lbl_Username = Label(self.root, text="Username")
        self.lbl_Username.place(x=14, y=47)

        self.fld_Username = Entry(self.root, width=20)
        self.fld_Username.place(x=94, y=48)

        self.lbl_Password = Label(self.root, text="Password")
        self.lbl_Password.place(x=14, y=94)

        self.fld_Password = Entry(self.root, width=20)
        self.fld_Password.place(x=96, y=96)

        self.btn_submit = Button(self.root, text="Submit", command=self.submit)
        self.btn_submit.place(x=125, y=144)

        self.root.mainloop()

    def submit(self):
        # Create a User Object
        # Fetch the Username and Password from Entries set to User object
        user = User()
        user.setUsername(self.fld_Username.get())
        user.setPassword(self.fld_Password.get())
        # Logincontroller()

        # Call the authentication method from logincontroller class pass the User object to validate-
        # user (Office staff or Seller) otherwise will not be given access to user
        results = LoginController().authentication(user)

        if results == 'Officestaff':
            # print the message login successfully
            # Destroy the current login window
            # Open the office staff dashboard
            mb.showinfo("System message", "Successfully login Office staff")
            self.root.destroy()

            # if the self.__results== office staff,it will open the office staff dashboard
            OfficeStaffDashboardView()

        elif results == 'Seller':
            # print the message successfully
            mb.showinfo("System message","Successfully login Seller")
            self.root.destroy()
            Seller_Dashboard()


        # if the self.__results==seller,it will open the seller dashboard
        else:
            # print the incorrect user name or password
            # otherwise give the chance to try again
            mb.showwarning("System message","Incorrect username or password")




LoginView()
