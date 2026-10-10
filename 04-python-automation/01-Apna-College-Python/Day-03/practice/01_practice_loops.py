# Practice: Loops
# Four short exercises written while learning loops.

# 1) Print all odd numbers from 1 to 20.
for number in range(1, 21):
    if number % 2 == 1:
        print(f"{number} is an odd number")

# 2) Print the multiplication table of 57 (from 1 to 10).
for i in range(1, 11):
    print(f"57 * {i} = {57 * i}")

# 3) Print all multiples of 3 from 1 to 50, but skip 15.
for number in range(1, 51):
    if number == 15:
        continue
    if number % 3 == 0:
        print(f"{number} is a multiple of 3")

# 4) Take two integers a and b as input.
#    Find and print the first number between 1 and 1000
#    that is divisible by both a and b.
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

for number in range(1, 1001):
    if number % a == 0 and number % b == 0:
        print(f"{number} is divisible by {a} and {b}")
        break