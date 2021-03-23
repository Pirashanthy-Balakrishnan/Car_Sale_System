class CarModel:
    def __init__(self, model_Id=None, model_name=None, price=None, manufacture_id=None):
        self.__modelId = model_Id
        self.__model_name = model_name
        self.__price = price
        self.__manufacture_id = manufacture_id

    def set_model_id(self, model_Id):
        self.__modelId = model_Id

    def set_model_name(self, model_name):
        self.__model_name = model_name

    def set_price(self, price):
        self.__price = price

    def set_manufactureid(self, manufacture_id):
        self.__manufacture_id = manufacture_id

    def get_modelid(self):
        return self.__modelId

    def get_modelname(self):
        return self.__model_name

    def get_price(self):
        return self.__price

    def get_manufacture_Id(self):
        return self.__manufacture_id
