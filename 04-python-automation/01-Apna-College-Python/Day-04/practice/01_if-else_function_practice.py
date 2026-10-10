# function to check if odd or even

x = int(input("Enter the number to check : "))

def checker(x):
    if(x % 2 == 0):
        print(f"{x} is even Number")
    else:
        print("odd number bro")

checker(x)