from a import a

class c(a):

    def pqr(self):
        print("from pqr c")

    def __init__(self, name, price):
        print("c con")
        self.price = price
        print(self.price)

        a.__init__(self, name)