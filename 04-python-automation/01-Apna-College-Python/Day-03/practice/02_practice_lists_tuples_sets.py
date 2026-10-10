# Practice: lists, tuples, and sets

# 1) Given a list of roll numbers, print all the UNIQUE roll numbers.
roll_numbers = [101, 105, 102, 101, 108, 105, 110]

unique_roll_numbers = set(roll_numbers)
print(unique_roll_numbers)

# 2) Employee records stored as a list of tuples.
#    Each tuple contains (employee_id, employee_name, salary).
#    Ask the user for an employee ID and search for it in the records.
records = [
    (101, "Ali", 50000),
    (102, "Ahmed", 60000),
    (103, "Sara", 55000)
]

search_id = int(input("Enter the employee ID: "))

for record in records:
    if search_id == record[0]:
        print("Here is the data:")
        print(record)
        break