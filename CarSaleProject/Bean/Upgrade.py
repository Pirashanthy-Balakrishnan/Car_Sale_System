class Upgrade:
    def __init__(self,reg_Num,component_id,price):
        self.__reg_Num = reg_Num
        self.__component_id = component_id
        self.__price = price

    def set_reg_Num(self,reg_Num):
        self.__reg_Num=reg_Num

    def set_component_id(self,component_id):
        self.__component_id=component_id

    def set_price(self,price):
        self.__price=price

    def get_reg_Num(self):
        return self.__reg_Num

    def get_component_id(self):
        return self.__component_id

    def get_price(self):
        return self.__price









