mynumber = "10"
number2 = "10"

sum = mynumber + number2
print("The sum of the numbers is: ", sum)

# 3. List: A list is a collection of items that are inside of square brackets.
"""A list is mutable ie you can change the contents of the list by adding/appending and alter it in different ways."""
mylist = ["Russia", "Germany", "Ukraine", "France", "Italy", "Spain"]

print(mylist)
print(type(mylist))

mylist.append("Poland")
mylist.append("Denmark")
print(mylist)

# We use the function insert() to add an item to the list at a specific index. The first argument is the index and the second argument is the item to be added.
mylist.insert(3, "Finland")
print(mylist)

# We use the function extend() to add multiple items to a list at once.
mylist.extend(["Switzerland", "Portugal"])
print(mylist)

# We use the function reverse() to reverse the order of items in a list.
mylist.reverse()
print(mylist)

# We use the sort() function to rearrange the items based in an alphabetical order.
mylist.sort()
print(mylist)

# We use the function pop() to remove an item from the list based on a given index.
mylist.pop(2)
print(mylist)

# We use the function remove() to remove an item based on the specific value name.
mylist.remove("Germany")
print(mylist)

# Create 2 lists with 3 items each and then join the two lists together into one big list.
list1 = ["Apple", "Google", "Samsung"]
list2 = ["Xiaomi", "Oppo", "Vivo"]
thelist = list1 + list2
print(thelist)

# 4. Tuple - This is an immutable type of list ie It is unchangeable. The way you define a tuple at first remains the same up to the end.
"""Introduced by use of parentheses instead of square brackets."""
presidents = ("Uhuru", "Ruto", "Yoweri", "Mnagangwa", "Ramaphosa")
print(presidents)
print(type(presidents))

# Note: Below code will bring an error.
# presidents.append("Suluhu")
# print(presidents)

# presidents.pop(2)
# print(presidents)