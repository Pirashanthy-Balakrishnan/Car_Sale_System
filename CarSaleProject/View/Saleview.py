from tkinter import *
from tkinter.ttk import Combobox
from currency_converter import CurrencyConverter
import datetime

from Bean.Sale import Sale
from Logic.Seller import Seller
from tkinter import messagebox as mb


class Saleview:

    def __init__(self,Reg_no,final_price):
        self.root=Tk()
        self.root.title("Sale_View")
        self.root.geometry('400x300+650+350')

        self.lbl_Reg_Num=Label(self.root, text="Reg_Num")
        self.lbl_Reg_Num.place(x=14, y=47)

        self.fld_Reg_Num=Entry(self.root ,width=20)
        self.fld_Reg_Num.place(x=130, y=48)
        self.fld_Reg_Num.insert(END,Reg_no)

        self.lbl_Final_amount= Label(self.root, text="Final_amount")
        self.lbl_Final_amount.place(x=14, y=96)

        self.fld_Final_amount = Entry(self.root, width=20)
        self.fld_Final_amount.place(x=130, y=96)
        self.fld_Final_amount.insert(END,final_price)

        self.lbl_Cuurency_Type = Label(self.root, text="Cuurency_Type")
        self.lbl_Cuurency_Type.place(x=14, y=144)

        self.combo_Currency_Type=Combobox(self.root,postcommand=self.take_Currency_type)
        self.combo_Currency_Type.place(x=130, y=144)

        self.btn_Conform=Button(self.root,text="Conform",command=self.Conform)
        self.btn_Conform.place(x=110, y=210)

        self.root.mainloop()

    def take_Currency_type(self):
        self.combo_Currency_Type["values"]= list(CurrencyConverter().currencies)

    def Conform(self):
        reg_No=self.fld_Reg_Num.get()
        final_amount=self.fld_Final_amount.get()
        select_Currency_Type=self.combo_Currency_Type.get()
        convert_Currency=CurrencyConverter().convert(final_amount,'GBP',select_Currency_Type)
        time_Stamp=datetime.datetime.now()
        sale=Sale(Time=time_Stamp,Finalamount=final_amount,Currency_Type=select_Currency_Type,Initial_Currency=convert_Currency,Reg_Num=reg_No)
        result=Seller().add_new_sell(sale)

        if result:

            mb.showinfo("Succesful Message","Successfully insert")
            self.root.destroy()
        else:
            mb.showwarning("Error message","Insert not Successful")





