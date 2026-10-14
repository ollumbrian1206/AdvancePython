# Python functions
# A function is a block of code that performs a given task.
# We have two main types of functions i.e:
# 1. User defined functions -> They are created by the user.
# 2. in-built function -> They come with the installation of the python interpreter. e.g print(), pop(), reverse(), sort() etc.

"""
1. User defined function. To create a user defined function, we use the def keyword followed by the name of the function, parenthensis and at the end of the function defination there is a full colon. The lines that comes next are indented and they mark the body of the function.

To invoke/call the function, you do so outside of the function body by the use of the function name.
"""

def greeting():
    print("Hello there. How are you doing?")

greeting()

# Example 2
print("============================")
# Below is a function that does some addition
def addition():
    number1 = 12
    number2 = 13
    number3 = 30
    sum = number1 + number2 + number3
    print("The sum of the numbers is: ", sum)

addition()

print("============================")

for greet in range(1, 6):
    greeting(), print(greet)

print("============================")
# Below is a function that demonstrates how one can pick details from the user on the keyboard.

def multiplication():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    product = number1 * number2
    print("The product of the two numbers is: ", product)

multiplication()

for x in range(3):
    multiplication()

# Create a function that is able to calculate the simple interest gained after a person inversted 75000 for 5 years and the rate was 6.5%. Formulae = si = (principal * rate * time) .
def simple_interest():
    principal = 75000
    rate = 6.5
    time = 5
    s_i = (principal * rate * time)/100
    print("The interest is: ", s_i)

simple_interest()