class p2:
    def abc(self):
        print("from p2 abc")

    def show(self):
        print("from p2 show")

    def __init__(self,age):
        self.age=age
        print("p2 con")
        print(self.age)