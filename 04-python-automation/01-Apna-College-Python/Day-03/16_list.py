# A list stores multiple values in an ordered collection.
# Lists are mutable: we can change, add, and remove items.
# A list can also store different data types.

marks = [10, 20, 30, 40, 50, "3", 3.5, True, False]

print(marks)              # print the whole list

# --- len() ---
# len() returns the number of items in the list.
print(len(marks))

# --- Indexing ---
# Items are indexed from 0: the first item has index 0.
print(marks[0])           # first item
print(marks[3])           # fourth item

# --- Negative indexing ---
# Negative indexes count from the end: -1 is the last item, -2 the second last.
print(marks[-1])          # last item
print(marks[-2])          # second last item

# --- Slicing ---
# Slice syntax: list[start:stop], the stop index is excluded.
# list[start:stop:step]
print(marks[1:4])         # items at index 1, 2, 3
print(marks[:3])          # from the beginning up to index 2
print(marks[2:5])         # items at index 2, 3, 4
print(marks[1:5:2])       # items at index 1 and 3 (step of 2)

# --- Loop through a list ---
print("Looping through marks:")
for mark in marks:
    print(mark)

# --- Membership (in) ---
# in checks whether a value exists in the list.
print(40 in marks)        # True
print(99 in marks)        # False

# --- Changing and adding values (mutability) ---
# A list with tool names used in DevOps.
tools = ["Linux", "Git", "Docker", "Python"]
print(tools)

tools[0] = "Ubuntu"       # change the first item
print(tools)

tools.append("AWS")       # add an item to the end
print(tools)

tools.insert(1, "Kubernetes")   # insert an item at index 1
print(tools)

# --- remove() and pop() ---
tools.remove("Docker")   # remove the first matching item
print(tools)

removed = tools.pop()    # remove and return the last item
print("removed:", removed)
print(tools)