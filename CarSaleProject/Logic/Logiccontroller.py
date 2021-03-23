from Model.LoginDAO import LoginDAO


class LoginController:
    def __init__(self):
        self.__userinfo=None

    def authentication(self, User):
    #create a model object and get the the user information
        self.__userinfo = LoginDAO().user_information()
        for row in self.__userinfo:


            if User.getUsername() == row[0] and User.getPassword() == row[1]:
                return row[2]

            # print(row)







