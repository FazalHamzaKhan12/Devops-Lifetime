# range() generates a sequence of numbers.
# It is very common to use it with loops.

# range(stop) -> numbers from 0 up to, but not including, stop.
# The stop value is always excluded.
print(list(range(5)))   # [0, 1, 2, 3, 4]

# range(start, stop) -> numbers from start up to stop - 1.
print(list(range(2, 10)))   # [2, 3, 4, 5, 6, 7, 8, 9]

# range(start, stop, step) -> jumps by step each time.
print(list(range(2, 10, 2)))  # [2, 4, 6, 8]

# Syntax reminder: range(start=0, stop, step=1)

# range() is commonly used inside a for loop.
for number in range(3):
    print(number)   # Prints 0, then 1, then 2.