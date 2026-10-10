# Type conversion / casting changes a value from one data type to another.
# Use int(), float() and str() to convert between types.

# Implicit casting: Python does it automatically.
# int + float = float
print(1 + 1.5)        # 2.5

# Explicit casting: we do it ourselves.
# int(1.5) becomes 1, so the result is a whole number.
print(1 + int(1.5))   # 2


# input() always returns a string.
# Convert it to an int when we need to do integer arithmetic.

# age = input("Enter your age: ")   # returns a string
# print(age + 1)                    # error: can't add int to str

age = int(input("Enter your age: "))   # convert to int first
print(age + 1)                         # now the math works