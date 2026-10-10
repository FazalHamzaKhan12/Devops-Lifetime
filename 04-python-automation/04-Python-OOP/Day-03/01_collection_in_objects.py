class Customer:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"I am, {self.name}, and i am {self.age}")


c1 = Customer("Nitish", 34)
c2 = Customer("Hamza", 19)
c3 = Customer("Bilal", 13)


L = [c1,c2,c3]

for i in L:
    i.intro()