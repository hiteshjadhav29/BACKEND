from account import account
class saving(account):
    def __init__(self,bankname,ifsc,AHname,ac_no,bal,FD):
        super().__init__(bankname,ifsc,AHname,ac_no)
        self.bal=bal
        self.FD=FD

    def display_saving(self):
        super().display_Account()
        return f"{self.bal} | {self.FD}"
    
    def deposit(self, amount):
        self.bal += amount
        print(f"{amount} deposited successfully.")
        print(f"Available Balance: {self.bal}")

    def withdraw(self, amount):
        if amount <= self.bal:
            self.bal -= amount
            print(f"{amount} withdrawn successfully.")
            print(f"Available Balance: {self.bal}")
        else:
            print("Insufficient Balance!")

    def buy_fd(self, amount):
        if amount <= self.bal:
            self.bal -= amount
            self.FD += amount
            print(f"FD of {amount} created successfully.")
            print(f"Available Balance: {self.bal}")
            print(f"Total FD Amount: {self.FD}")
        else:
            print("Insufficient Balance to create FD")

obj = saving("HDFC","1234","Hitesh","123",999999,2)
print(obj.bankname)
print(obj.ifsc)
print(obj.AHname)
print(obj.ac_no)
print(obj.bal)
print(obj.FD)

obj.deposit(5000)
obj.withdraw(2000)
obj.buy_fd(100000)

print("\nFinal Details:")
print(obj.display_saving())
