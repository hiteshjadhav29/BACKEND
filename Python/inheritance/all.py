print("\n===== TYPES OF INHERITANCE =====")
print("1. Single Inheritance")
print("2. Multiple Inheritance")
print("3. Multilevel Inheritance")
print("4. Hierarchical Inheritance")
print("5. Hybrid Inheritance")

choice = int(input("\nEnter your choice (1-5): "))

match choice:

    # Single Inheritance
    case 1:
        print("\n--- SINGLE INHERITANCE ---")

        class Animal:
            def eat(self):
                print("Animal can eat.")

        class Dog(Animal):
            def bark(self):
                print("Dog can bark.")

        obj = Dog()
        obj.eat()
        obj.bark()

    # Multiple Inheritance
    case 2:
        print("\n--- MULTIPLE INHERITANCE ---")

        class Father:
            def father_property(self):
                print("Father owns a house.")

        class Mother:
            def mother_property(self):
                print("Mother owns jewellery.")

        class Child(Father, Mother):
            def child_property(self):
                print("Child inherits from both Father and Mother.")

        obj = Child()
        obj.father_property()
        obj.mother_property()
        obj.child_property()

    # Multilevel Inheritance
    case 3:
        print("\n--- MULTILEVEL INHERITANCE ---")

        class Grandfather:
            def land(self):
                print("Grandfather owns land.")

        class Father(Grandfather):
            def house(self):
                print("Father owns a house.")

        class Son(Father):
            def bike(self):
                print("Son owns a bike.")

        obj = Son()
        obj.land()
        obj.house()
        obj.bike()

    # Hierarchical Inheritance
    case 4:
        print("\n--- HIERARCHICAL INHERITANCE ---")

        class Person:
            def details(self):
                print("Person has name and age.")

        class Student(Person):
            def study(self):
                print("Student studies in college.")

        class Employee(Person):
            def work(self):
                print("Employee works in a company.")

        s = Student()
        e = Employee()

        print("\nStudent Object:")
        s.details()
        s.study()

        print("\nEmployee Object:")
        e.details()
        e.work()

    # Hybrid Inheritance
    case 5:
        print("\n--- HYBRID INHERITANCE ---")

        class Grandparent:
            def gp(self):
                print("Grandparent property.")

        class Father(Grandparent):
            def father(self):
                print("Father property.")

        class Mother(Grandparent):
            def mother(self):
                print("Mother property.")

        class Child(Father, Mother):
            def child(self):
                print("Child inherits from Father and Mother.")

        obj = Child()

        obj.gp()
        obj.father()
        obj.mother()
        obj.child()

    case _:
        print("Invalid Choice!")