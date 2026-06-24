from abc import ABC, abstractmethod



class Login(ABC):

    @abstractmethod
    def get_credentials(self):
        pass

    @abstractmethod
    def validate(self):
        pass



class User(Login):
    def __init__(self):
        self.username = ""
        self.password = ""

    def get_credentials(self):
        self.username = input("Enter Username: ")
        self.password = input("Enter Password: ")

    def validate(self):
        
        valid_username = "user123"
        valid_password = "userpass"

        if self.username == valid_username and self.password == valid_password:
            print("Correct Username and Password")
        else:
            print("Invalid Username or Password")



class Admin(Login):
    def __init__(self):
        self.email = ""
        self.password = ""

    def get_credentials(self):
        self.email = input("Enter Admin Email: ")
        self.password = input("Enter Password: ")

    def validate(self):
        
        valid_email = "admin@example.com"
        valid_password = "admin123"

        if self.email == valid_email and self.password == valid_password:
            print("Correct Email and Password")
        else:
            print("Invalid Email or Password")



choice = input("Login as User or Admin (u/a): ").lower()

if choice == 'u':
    user = User()
    user.get_credentials()
    user.validate()

elif choice == 'a':
    admin = Admin()
    admin.get_credentials()
    admin.validate()

else:
    print("Invalid Choice")