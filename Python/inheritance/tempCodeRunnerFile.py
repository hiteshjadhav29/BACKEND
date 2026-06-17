class bank:
    bankname="hdfc"
    ifsc="1234"
    def __init__(self,bankname,ifsc):
        self.bankname=bankname
        self.ifsc=ifsc
    def display_bank(self):
        return f"{self.bankname}  |  {self.ifsc}"
