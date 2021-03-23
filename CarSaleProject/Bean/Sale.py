class Sale:
    def __init__(self,Sale_id=None,Time=None,Finalamount=None,Currency_Type=None,Initial_Currency=None,Reg_Num=None):
        self.__Reg_Num = Reg_Num
        self.__Initial_Currency = Initial_Currency
        self.__Currency_Type = Currency_Type
        self.__Finalamount = Finalamount
        self.__Time = Time
        self.__Sale_id = Sale_id


    def setSale_id(self,Sale_id):
        self.__Sale_id=Sale_id

    def setreg_Num(self,Reg_Num):
        self.__Reg_Num=Reg_Num

    def set_time(self,Time):
        self.__Time=Time

    def set_final_amount(self,Finalamount):
        self.__Finalamount=Finalamount



    def set_Currency_Type(self,Currency_Type):
        self.__Currency_Type=Currency_Type

    def set_Initial_Currency(self,Initial_Currency):
        self.__Initial_Currency=Initial_Currency



    def getSale_id(self):
        return self.__Sale_id

    def getreg_Num(self):
       return self.__Reg_Num

    def get_time(self):
        return self.__Time

    def get_final_amount(self):
        return self.__Finalamount



    def get_Currency_Type(self):
       return self.__Currency_Type

    def get_Initial_Currency(self):
        return self.__Initial_Currency











