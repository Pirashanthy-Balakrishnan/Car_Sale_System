class User:
    def __init__(self):
        self.__username=None
        self.__passsword=None
    def setUsername(self,uname):
        self.__username=uname
    def getUsername(self):
        return self.__username
    def setPassword(self,pwd):
        self.__passsword=pwd
    def getPassword(self):
        return self.__passsword

