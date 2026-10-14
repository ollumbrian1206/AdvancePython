# Conditional statements.

# By use of an if statement, create a python program that evaluates whether a person can donate blood based on the age and the weight. If the age is greater than 15 and weight greater than 51, the person can donate blood. Otherwise, the person cannot.
age = 12
weight = 47

if age > 15 and weight > 51:
    print("Can donate blood.")
else: 
    print("Cannot donate blood.")

# How do you pick user's input from the terminal?
# We use the input() function to pick details/input from the terminal. 
# Below we demonstrate the aspect of typecasting.

age = int(input("Kindly enter your age:"))

print("The age entered is:", age)
print("The datatype of age is:", type(age))
