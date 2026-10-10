import sys

def addition(num1, num2):
    add = num1 + num2
    return add

def subtraction(num1, num2):
    sub = num1 - num2
    return sub

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    output = addition(num1, num2)
    print(output)
elif operation == "sub":
    output = subtraction(num1 , num2)
    print(output)
else:
    print("Error")