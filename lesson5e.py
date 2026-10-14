class Farmer:
    def __init__(self):
        self.name = "John"
        self.litres = 50

    def farmer_info(self):
        print("The name of the farmer is: ", self.name)
        print("The number of litres the farmer provided: ", self.litres)


# Below we create an object of the class Farmer
farmer1 = Farmer()

# Below, by the use of the dot notation method, we can be able to access the method inside of the class farmer.
farmer1.farmer_info()