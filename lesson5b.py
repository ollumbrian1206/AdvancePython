class Car:
    pass

# Below we create three cars from our class of Car
car1 = Car()
car2 = Car()
car3 = Car()

print(car1, car2, car3)

# Below we give our different objects some attributes.
car1.brand = "Toyota"
car1.model = "Camry"

print("Car1: ", car1.brand, car1.model)
# Above we use the dot notation to access the items of an object.

car2.brand = "Honda"
car2.model = "Civic"
print("Car2: ", car2.brand, car2.model)

# Create the attribute of object three of the car.
car3.brand = "Ford"
car3.model = "Mustang"
print("Car3: ", car3.brand, car3.model)