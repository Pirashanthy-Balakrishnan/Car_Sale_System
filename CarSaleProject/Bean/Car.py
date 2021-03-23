class Car:
    def __init__(self,Reg_Num=None,Colour=None,Num_Doors=None,Model_id=None):
        self.__Reg_Num=Reg_Num
        self.__Colour=Colour
        self.__Num_Doors=Num_Doors
        self.__Model_id=Model_id

    def setRegNum(self,Reg_Num):
        self.__Reg_Num=Reg_Num

    def setColour(self,Colour):
        self.__Colour=Colour

    def setNumDoors(self,NumDoors):
        self.__Num_Doors=NumDoors

    def setModelid(self,Model_id):
        self.__Model_id=Model_id

    def getRegNum(self):
        return self.__Reg_Num

    def getColour(self):
        return self.__Colour

    def getNumDoors(self):
        return self.__Num_Doors

    def getModelid(self):
        return self.__Model_id

