from tkinter import *
from tkinter.ttk import Combobox

from Logic.Staff import Officestaff
from tkinter import messagebox as mb




class SearchCarView:
    def __init__(self):
        self.root=Tk()
        self.root.title("Search Car")
        self.root.geometry('300x200+600+300')

        self.lbl_select_Model= Label(self.root, text="selectModel")
        self.lbl_select_Model.place(x=14, y=47)

        self.combo_select_Model = Combobox(self.root, postcommand=self.select_Model)
        self.combo_select_Model.place(x=130, y=47)


        self.lbl_select_Manufacture = Label(self.root, text="selectManufacture")
        self.lbl_select_Manufacture.place(x=14, y=94)

        self.combo_select_Manufacture = Combobox(self.root, postcommand=self.select_Manufacture)
        self.combo_select_Manufacture.place(x=130, y=94)

        self.btn_submit = Button(self.root, text="Search", command=self.search)
        self.btn_submit.place(x=125, y=144)

        self.btn_Back = Button(self.root, text="Back", command=self.back)
        self.btn_Back.place(x=40, y=144)

        self.root.mainloop()



    def select_Model(self):
        self.combo_select_Model["values"] = Officestaff().takeModelname()



    def select_Manufacture(self):
        self.combo_select_Manufacture["values"] = Officestaff().takemanufacturename()


    def search(self):
        if self.combo_select_Model.get() == "" and self.combo_select_Manufacture.get() == "":
            mb.showwarning("System message","select at least one of above model name or Manufacture name")
        else:
            result  =Officestaff().searchCar(self.combo_select_Model.get(),self.combo_select_Manufacture.get())
            print(result)


            temp_Window = Tk()
            temp_Window.title("Search result")

            for i in range(len(result)):
                for j in range(len(result[0])):
                    temp_Entry=Entry(temp_Window,width=10,fg="red")
                    temp_Entry.grid(row=i,column=j)
                    temp_Entry.insert(END,result[i][j])
            temp_Window.mainloop()
    def back(self):
        self.root.destroy()
        from View.OfficeStaffDashboardView import OfficeStaffDashboardView
        OfficeStaffDashboardView()



