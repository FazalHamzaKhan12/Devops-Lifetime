# Assignment operators store ("assign") a value into a variable.
# Short forms combine an operation with = .

# Basic assignment
x = 1
print(x)        # 1

# These two lines do the same thing: add 1 to x.
x = x + 1       # long way
print(x)        # 2

x = 1
x += 1          # short way:  x = x + 1
print(x)        # 2

# Other assignment operators
y = 10
y -= 5          # y = y - 5
print(y)        # 5

z = 6
z *= 2          # z = z * 2
print(z)        # 12

w = 20
w /= 4          # w = w / 4
print(w)        # 5.0
