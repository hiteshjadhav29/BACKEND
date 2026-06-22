from b import b
from c import c

class d(b, c):

    def mno(self):
        print("from mno d")

    def __init__(self, name, age, price, qty):
        print("d con")
        self.qty = qty

        b.__init__(self, name, age)
        c.__init__(self, name, price)

obj = d("ram", 18, 5000, 10)

obj.abc()
obj.mno()
obj.pqr()
obj.xyz()