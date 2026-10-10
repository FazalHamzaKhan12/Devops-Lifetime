# class Customer:

#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender


# def greet(customer):
#     if customer.gender == "Male":
#         print("hello", customer.name, "Sir")
#     else:
#         print("Hello", customer.name, "Ma'am")

#     cust2 = Customer("Hamza", "Male")
#     return cust2

# cust = Customer("Nitish", "Male")

# new_cust = greet(cust)
# print(new_cust.name)
# # greet(cust)
# # print(cust.name)


#  =================================

class Customer:

    def __init__(self, name):
        self.name = name



def greet(customer):
    print(id(customer))

cust = Customer("Hamza")

print(id(cust))
greet(cust)

