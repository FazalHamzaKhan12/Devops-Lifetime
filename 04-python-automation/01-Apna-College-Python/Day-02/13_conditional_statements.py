# Conditional statements decide which code runs
# based on whether a condition is True or False.

# if - runs the code only when the condition is True.
age = 20

if age >= 18:
    print("You are old enough to vote.")

# if / else - one block runs when True, another when False.
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# if / elif / else - checks several conditions in order.
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")