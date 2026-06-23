import random
class login:
    def __init__(self,name,username,pwd):
        self.name=name
        self.username=username
        self.__pwd=pwd
        self.__otp=None
    
    def enter_otp(self,num):
        if num==self.__otp:
            print("navigating to home page")
        else:
            print("invalid otp")

    def login(self,username,pwd):
        if self.username==username and self.__pwd==pwd:
            print("login sucessful")
            self.__otp=random.randint(1000,2000)
            print("otp: ",self.__otp)
            otp=int(input("enter otp"))
            self.enter_otp(otp)
        else:
            print("invalid user or pass")

obj=login("ram","ram@123",123)
obj.login("ram@123",123)


