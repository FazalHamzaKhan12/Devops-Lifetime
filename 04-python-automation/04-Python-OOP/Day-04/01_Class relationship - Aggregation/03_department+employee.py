class Employee:

    def __init__(self, name):
        self.name = name


class Department:

    def __init__(self, name, employee):
        self.name = name

        # Department HAS-A Employee        
        self.employee = employee

# Employee exists independently
emp1 = Employee("Fazal Hamza Khan")

# Existing Employee object is passed to Department
department1 = Department("Devops", emp1)

print(department1.name)
print(department1.employee.name)


