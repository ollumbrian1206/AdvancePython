# Conditional statements.
# If ... else statements.

# number = int(input("Enter your number:"))

# if number > 0:
    #print("The number is positive.")
# else:
    # print("The number is negative.")

# print("===========================")
# Create a dictionary with students details like name, email, admissionNo and password. Prompt the student to enter the password for him to be able to access the student portal. By use of an if statement, check whether the entered password to navigate him to the portal, otherwise, pass a message to block the student from accessing the student portal.

student_details = {
    "name" : "Brian Ollum",
    "email" : "ollumbrian1206@gmail.com",
    "admissionNo" : "264",
    "password" : "123456"
}

portal_password = input("Enter your password: ")

if portal_password == student_details["password"]:
    print("Access granted")
else:
    print("Incorrect password. Try again.")

print("=========================")
# Combining the logical and comparison operators together.
age = int(input("Enter your current age: "))
has_id = True

if age >= 18 and has_id:
    print("You can join us for the function.")
else:
    print("Sorry, you do not qualify to join us.")

print("==========================")
# Below is an example of a nested if statement.
if age >= 18:
    if has_id:
        print("You qualify. You can join us.")
    else:
        print("You do not qualify because you need an id.")
else:
    print("You do not qualify because you are underage.")

print("==========================")
# By use of a nested if statement, check whether a person is allowed to drive or not. For a person to be allowed to drive, they need to be above 18 years and have a valid driver license.

age = int(input("Enter your age: "))
has_valid_dl = True
if age >= 18:
    if has_valid_dl:
        print("You are qualified to drive a vehicle.")
    else:
        print("You do not qualify because you need a valid driving license.")
else:
    print("You do not qualify to drive because you are underage.")