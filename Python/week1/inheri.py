class Engine:
    def __init__(self, cc, horsepower):
        self.cc = cc
        self.horsepower = horsepower

    def display_engine(self):
        return f"{self.cc}, {self.horsepower}"


class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.engine = Engine("100", "200")

    def display_car(self):
        return f"{self.name}, {self.price}"

    def display_all(self):
        return f"{self.display_car()} | {self.engine.display_engine()}"


obj = Car("bmw", "1cr")
print(obj.display_all())