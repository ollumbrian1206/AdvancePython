# Python OOP -> It enables us to organize code into objects. 
# An object is a real world thing that has attributes/features/characteristics and functions/methods/actionables.
# A class is a blueprint from which objects can be created from.


class Employee:
    def __init__(self):
        print("Employee Created")

# To create a class we use the "class" keyword followed by the name of the class and since our class does not contain any attribute or behaviour, we use the keyword pass


# Below we create an object called "employee1" from the class of Employee()
employee1 = Employee()
employee2 = Employee()
