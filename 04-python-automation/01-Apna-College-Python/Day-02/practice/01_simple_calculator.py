# A simple calculator, built with if / elif / else.

print("Welcome to the Simple Calculator!")

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    print(f"{first} + {second} = {first + second}")
elif operation == "-":
    print(f"{first} - {second} = {first - second}")
elif operation == "*":
    print(f"{first} * {second} = {first * second}")
elif operation == "/":
    print(f"{first} / {second} = {first / second}")
else:
    print("Invalid operation!")