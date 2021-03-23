class Accessories:
    def __init__(self,component_Name=None,component_id=None,price=None):
        self.__component_Name = component_Name
        self.__component_id = component_id
        self.__price = price

    def set_component_Name(self,component_Name):
        self.__component_Name=component_Name

    def set_component_id(self,component_id):
        self.__component_id=component_id

    def set_price(self,price):
        self.__price=price

    def get_component_Name(self):
        return self.__component_Name

    def get_component_id(self):
        return self.__component_id

    def get_price(self):
        return self.__price


