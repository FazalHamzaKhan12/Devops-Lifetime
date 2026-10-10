class Address:

    def __init__(self,city,pincode):
        self.city = city
        self.pincode = pincode


class Customer:

    def __init__(self, name, address):
        self.name = name

        # here is we create HAS-A Address
        self.address = address

# Address object is created separately
address1 = Address("Batkhela", 12354)

# Existing Address object is passed to Customer
customer1 = Customer("Fazal Hamza", address1)

print(customer1.name)
print(customer1.address.city)




# Customer ─── HAS-A ───► Address

