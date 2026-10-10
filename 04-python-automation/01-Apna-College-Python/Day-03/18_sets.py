# A set stores UNIQUE values only.
# If we pass duplicate values, Python removes them automatically.

# --- Creating a set ---
# Sets use curly braces {}, but they do NOT store key-value pairs.
marks = {98, 33, 95, 1, 98}     # 98 appears twice
print(marks)                    # 98 appears only once

# Note: sets are unordered, so the print order may vary.

# --- No indexing ---
# Sets do NOT support indexing like lists or tuples.
# The line below is NOT allowed and would raise a TypeError:
# print(marks[0])

# --- Empty set: {} vs set() ---
# {} creates an empty DICTIONARY (covered in 19_dictionary.py).
# set() creates an empty SET.
empty_set = set()
empty_dict = {}
print(type(empty_set))     # <class 'set'>
print(type(empty_dict))    # <class 'dict'>

# --- add() and remove() ---
# Sets are mutable: we can add and remove values.
tools = {"Linux", "Docker", "Git"}
print(tools)

tools.add("Python")       # add one value
print(tools)

tools.add("Linux")        # already exists -> nothing changes
print(tools)

tools.remove("Docker")    # remove one value
print(tools)

# discard() is safer than remove(): it does NOT raise an error
# if the value is not in the set.
tools.discard("AWS")      # not in the set -> no error
print(tools)

# --- Membership (in) ---
print("Linux" in tools)   # True
print("AWS" in tools)     # False

# --- Loop through a set ---
for tool in tools:
    print(tool)

# --- Set operations ---
devops = {"Linux", "Docker", "Python", "AWS"}
cloud = {"AWS", "Azure", "GCP"}

# union(): all values from both sets
print(devops.union(cloud))

# intersection(): values present in BOTH sets
print(devops.intersection(cloud))   # AWS

# difference(): values in devops but NOT in cloud
print(devops.difference(cloud))