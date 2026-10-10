class Parent:

    def __init__(self, name):
        self.name = name
        print("yaha 1 ka nahi")


class Child(Parent):

    def __init__(self, name , age):
        
        super().__init__(name)
        print("yaha 2 aygaa ka nahi")
        self.age = age

c = Child("Hamza", 19)

print(c.name)
print(c.age)