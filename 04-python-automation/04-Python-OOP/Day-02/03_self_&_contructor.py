class Computer:

    def __init__(self):
        self.name = "Hamza"
        self.age = 20

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

c1.name = "king"
c2.age = 20

c1.update()

if c1.compare(c2):
    print("They are same")

print(c1.name)
print(c2.age)


print(id(c1))