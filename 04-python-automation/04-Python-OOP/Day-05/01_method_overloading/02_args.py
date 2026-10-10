class Calculator:
    def add(self, *numbers):
        total = 0

        for number in numbers:
            total += number

        return total

obj = Calculator()

# obj.add(2)
# obj

print(obj.add(20,20))
print(obj.add(20,20,30))
print(obj.add(20,20,90,20))
