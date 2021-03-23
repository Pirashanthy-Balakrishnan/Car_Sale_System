# def sum(x,y):
#     print(x+y)
#
# sum(4,5)
class Logic:
    def result(self,a):
        # print(a)
        return a+"world"

class UI:
    def call(self):
        Logic().result("hello")

UI().call()