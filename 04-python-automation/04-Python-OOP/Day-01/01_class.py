class Dog:
    def __init__(self, name , breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        
    def bark(self):
        print("woof whoof")
        
class Owner:
    def __init__(self, name, address, phNO):
        self.name = name
        self.address = address
        self.phno = phNO


owner1 = Owner("Hamza", "SouthPakistan", "03432423483")   
dog = Dog("hero", "german", owner1)
print(dog.owner.name)
    
    