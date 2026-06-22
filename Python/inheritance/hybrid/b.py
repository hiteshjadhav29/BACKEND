from a import a

class b(a):

    def abc(self):
        print("from abc b")

    def __init__(self, name, age):
        print("b con")
        self.age = age
        print(self.age)

        a.__init__(self, name)