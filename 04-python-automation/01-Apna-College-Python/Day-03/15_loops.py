# Loops repeat a block of code.
# Python has two main loops: for and while.

# --- for loop with range() ---
# range(start, stop) gives numbers from start up to stop - 1.
print("for loop with range():")
for number in range(1, 6):
    print(number)

# range(start, stop, step) jumps by step each time.
print("\nfor loop with a step:")
for number in range(2, 10, 2):   # 2, 4, 6, 8
    print(number)

# --- while loop ---
# A while loop repeats while a condition is True.
# We must update the counter, otherwise the loop never ends.
print("\nwhile loop:")
count = 1
while count <= 5:
    print(count)
    count += 1   # increase count by 1 each time

# --- break ---
# break stops the loop immediately.
print("\nbreak example:")
for number in range(10):
    if number == 5:
        break   # exit the loop when number reaches 5
    print(number)

# --- continue ---
# continue skips only the current iteration.
print("\ncontinue example:")
for number in range(5):
    if number == 2:
        continue   # skip 2 and move on to the next number
    print(number)

# --- Loop through a list ---
# We can loop through any collection: list, tuple, set, dictionary, string.
print("\nloop through a list:")
servers = ["web-01", "web-02", "db-01"]
for server in servers:
    print(server)

# --- Loop through a string ---
# A string is a collection of characters.
print("\nloop through a string:")
name = "Python"
for character in name:
    print(character)

# --- Example: triangle pattern with a while loop ---
# "*" * i repeats the star i times, printing one line at a time.
i = 1
while i <= 5:
    print("*" * i)
    i += 1

# --- Example: even numbers from 0 to 5 ---
# % returns the remainder, so a number is even when number % 2 == 0.
for number in range(0, 6):
    if number % 2 == 0:
        print(number, "is even")

# --- Example: multiples of 3 from 1 to 50, skipping 21 ---
# Combines range(), % and continue in one example.
for number in range(1, 51):
    if number == 21:
        print("21 found, skipping it")
        continue
    if number % 3 == 0:
        print(number, "is a multiple of 3")