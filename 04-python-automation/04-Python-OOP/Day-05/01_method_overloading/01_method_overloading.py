class Calculator:
    def add(self, a, b=0):
        return a + b


obj = Calculator()


print(obj.add(4, 30))
print(obj.add(4))

# Key idea: One method can work with one or two arguments because b has a default value.
