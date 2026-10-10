# Strings have built-in methods that let us inspect or change the text.

name = "alice"

# Convert the whole string to upper/lower case.
print(name.upper())       # ALICE
print(name.lower())       # alice
print(name.capitalize())  # Alice (first letter only)

# find() returns the index (position) of the first matching character.
# Indexes start counting from 0.
print(name.find('l'))     # 2
print(name.find('z'))     # -1 means the character was not found

# replace() swaps one part of the string for another.
print(name.replace('a', 'F'))  # Glice

# in checks whether a string contains another value.
# It returns True or False.
print('a' in name)       # True
print('z' in name)       # False


# startswith() checks whether a string begins with a certain value.
hero = input("Enter a superhero name: ")
print("Superhero name is:", hero)
print("Does it start with 'S'?", hero.startswith('S'))