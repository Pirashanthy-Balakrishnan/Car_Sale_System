class Manufacture:
    def __init__(self,manufacture_id=None,manufacturename=None):

        self.__manufacture_id=manufacture_id
        self.__manufacturename=manufacturename

    def setmanufacture_id(self,manufacture_id):
        self.__manufacture_id=manufacture_id

    def setmanufacturename(self,manufacturename):
        self.__manufacturename=manufacturename

    def getmanufacture_id(self):
        return self.__manufacture_id

    def getmanufacturename(self):
        return self.__manufacturename




