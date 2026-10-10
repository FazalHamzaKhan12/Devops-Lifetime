# Personal details: take a user's name, then print their info.

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

age = 27
height = 1.75

# Join text and variables with +, converting numbers with str().
print("Hello, " + first_name + " " + last_name + "!")
print(first_name + "'s age is " + str(age))
print(first_name + "'s height is " + str(height) + "m")