from animal import animal
class dog(animal):
    def __init__(self):
        print("child class")

    def __init__(self,name,weight):
        super().__init__(name,weight)

    def all_details(self):
        super().greet()
        print(f"{self.name}   |  {self.weight}")
        



obj = dog("pitbull","10kg")
print(obj.name)
print(obj.weight)
obj.greet()
print(obj.all_details())