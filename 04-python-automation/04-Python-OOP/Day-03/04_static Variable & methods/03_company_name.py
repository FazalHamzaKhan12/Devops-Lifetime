class Employee:

    # Static/Class variable
    # All employees belong to the same company
    company = "Fz Labs"

    def __init__(self, name, salary):
        # These are instance variables
        # Every employee has their own values
        self.name = name
        self.salary = salary


e1 = Employee("Hamza", 100000)
e2 = Employee("Ali", 80000)

print(e1.name)
print(e1.company)

print(e2.name)
print(e2.company)