# We can pass parameters to the constructor as demonstrated below
class Farmer:
    def __init__(self, name, litres, price):
        self.name = name
        self.litres = litres
        self.price = price

    def calculate_payment(self):
        return self.litres * self.price

# From the above, we can be able to create different objects with different details
farmer1 = Farmer("John", 50, 55)
farmer2 = Farmer("Mary", 38, 55)
farmer3 = Farmer("Joseph", 70, 55)

print("Farmer1 :", farmer1.name, farmer1.litres, "He is going to be paid:", farmer1.calculate_payment())

print("Farmer2 :", farmer2.name, farmer2.litres, "She is going to be paid:", farmer2.calculate_payment())

print("Farmer3 :", farmer3.name, farmer3.litres, "He is going to be paid:", farmer3.calculate_payment())