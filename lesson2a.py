# Dictionary - A datatype in python that stores value in key-value pairs. The key of a dictionary needs to be unique/immutable while the value can be an integer, string, tuple, list, or even another dictionary.
# Dictionaries are introduced by use of curly braces.
 
phonebook = {
    "Jena" : 2547478993649,
    "Norah" : 256749085664,
    "Bella" : 255746353638
    }  
print("My phonebook dictionary is:", phonebook)

# To access the values of a dictionary, we use the key.
print("Norah's phone number is:", phonebook["Norah"])

print("===========================")

player = {
    "name" : "Messi",
    "age" : 39,
    "teams" : ["Miami", "PSG", "Argentina", "Barcelona"],
    "more" : {
        "children" : 3,
        "networth" : 4.5,
        "citizenship" : ("USA", "Spain", "Argentina")
    }}

print(player["more"]["citizenship"][2])

print("===========================")

student_profile = {
    "name" : "Brian",
    "age" : 18,
    "subjects" : ["Python", "Database", "Networking"],
    "details" : {
        "phone" : 254712345678,
        "location" : "Nairobi",
        "marks" : {
            "Python" : 85,
            "Database" : 78,
            "Networking" : 90
        }
    }
}

print("The student's name is:", student_profile["name"])
print("One of the subjects the student undertakes is:",student_profile["subjects"][1])
print("The student's phone number is:", student_profile["details"]["phone"])
print("The student's location is:", student_profile["details"]["location"])
print("The student's marks in python is:", student_profile["details"]["marks"]["Python"])
print("The student's marks in Networking is:", student_profile["details"]["marks"]["Networking"])

print("===========================")
# Boolean - It evaluates to either True or False.
isSunny = True
isRaining =False

print("Is today Sunny in Nairobi?", isSunny)
print(type(isSunny))