# Logical operators combine boolean expressions
# and return a single boolean value (True or False).

# and -> True only if both sides are True.
# or  -> True if at least one side is True.
# not -> Reverses the value: True becomes False.

first = 5 > 10     # False
second = 5 > 2     # True

print(first and second)   # False, because first is False
print(first or second)    # True,  because second is True
print(not first)          # True,  because first is False

# Logical operators are often used with real conditions.
age = 20

print(age >= 18 and age <= 60)   # True,  both conditions are True
print(age < 18 or age > 60)      # False, neither condition is True
print(not age < 18)              # True,  because age is not below 18