# if ... elif ... else conditional statement.
# It is used to evaluate multiple conditions.

# Below is an example of the menu tab on the Bank.

print("Kindly enter an option. \n 1. Deposit \n 2. Send money \n 3. Withdraw money \n 4. Check balance \n 5. Exit")
options = int(input("Enter the option: "))

if options == 1:
    print("You selected Deposit.")
elif options == 2:
    print("You selected Send money.")
elif options == 3:
    print("You selected Withdraw money.")
elif options == 4:
    print("You selected Check balance.")
elif options == 5:
    print("You selected Exit. Thank you!")
else:
    print("Please enter a valid option from 1 to 5.")

print("============================")
# By use of the if... elif... else conditional statement, create a python statement that is able to show the working mechanism of the traffic lights.

print("There are 3 traffic light options. \n 1. Go. \n 2. Get ready. \n 3. Stop")
options = int(input("Enter an option: "))

if options == 1:
    print("The light is green.")
elif options == 2:
    print("The light is amber.")
elif options == 3:
    print("The light is red.")
else:
    print("Error. Please enter a valid option.")