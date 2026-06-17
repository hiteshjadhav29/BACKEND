class animal:
    type = "animal"

    def __init__(self):
        print("default animal constructor")
    
    def __init__(self,name ,weight):
        self.name=name
        self.weight=weight

    def xyz(self):
        print("hello from parent class")

    def greet(self):
        print("hello im an animal")