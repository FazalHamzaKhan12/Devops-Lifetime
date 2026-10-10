# we disucssed about the conditional statements in python

if 5 > 2:
    print("5 is greater than 2")



rain = input("Is it raining? (yes/no): ")
rain = rain.lower()  # Convert input to lowercase for consistency

if rain == "yes":
    print("Take an umbrella.")
elif rain == "no":
    print("No need for an umbrella.")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")




grade = 'A'

if grade == 'A':
    print("Excellent!")
elif grade == 'B':
    print("Good job!")
elif grade == 'C':
    print("You can do better.")
else:
    print("Invalid grade.")