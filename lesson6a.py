# Inheritance
# Parent Class
class Person:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print("Person information")

# Child class
class Farmer(Person):
    def __init__(self, name, litres):
        super().__init__(name)
        self.litres = litres

    def display_info(self):
            print("Farmer information") # This is overriding inheritance.
            # return super().display_info()

farmer1 = Farmer("Mike", 30)
farmer1.display_info()