# a code to learn try except in python


# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("Division by zero is not allowed.")
# finally:
#     print("This block will always execute, regardless of whether an exception occurred or not.")
# print("\nbye!")





# Another example of try except in python

def addNumbers(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Both inputs must be numbers."
    # except NameError:
    #     return "Error: One or both variables are not defined."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

print(addNumbers(10, 2)) 
print(addNumbers(30, 1))
print(addNumbers(20, "a"))
print(addNumbers(4, 2))
print("All numbers added successfully!")


# Here  you see i got error in last 2 print statements
# so let's use try except in this code
