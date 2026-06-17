from bank import bank
class account(bank):
    def __init__(self,bankname,ifsc,AHname,ac_no):
        super().__init__(bankname,ifsc)
        self.AHname=AHname
        self.ac_no=ac_no

    def display_Account(self):
        super().display_bank()
        return f"{self.ac_no} | {self.AHname}"

        