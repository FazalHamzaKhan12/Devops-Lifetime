class Customer:

    # Static/Class variable
    # Shared by all Customer objects
    bank_name = "UBL"

    def __init__(self, name):
        # Instance variable
        # Each customer has their own name
        self.name = name


c1 = Customer("Hamza")
c2 = Customer("Bilal")

print(c1.name)
print(c2.name)

# Both objects can access the same static variable
print(c1.bank_name)
print(c2.bank_name)