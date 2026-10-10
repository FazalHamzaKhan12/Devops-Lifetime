day_of_week = input("Enter the day of week!: ").lower()

print(day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday":
    print("i will learn LIVE DEVOPS")
else:
    print("I will practice DevOps")
    
    
    
choice = input("Enter the operations: (options: +, -, *, /, %)")

if choice == "+":
    print("addition")
elif choice == "-":
    print("subtraction")
elif choice == "*":
    print("Multiplication")
elif choice == "/":
    print("division")
else: 
    print("invalid options")