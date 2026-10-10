# Variables store values in memory.
# They are called "variables" because the value can change during the program.

name = "Fazal Hamza Khan"
age = 27

print(name)
print(age)

# Use the + operator to join (concatenate) text and variables.
# str() converts a number to a string so it can be joined with text.
print("My name is " + name + " and I am " + str(age) + " years old.")


# Variable naming rules:
# - Use clear, meaningful names (snake_case)
# - Start with a letter or underscore
# - Do NOT use reserved keywords (e.g. True, False, None, if, for)

# name = "Fazal"          # ok
# user_first_name = "..." # ok, readable
# True = "not allowed"    # error: True is a Python keyword