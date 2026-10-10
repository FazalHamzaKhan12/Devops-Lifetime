# A tuple stores multiple values in an ordered collection.
# Tuples are IMMUTABLE: once created, the values cannot be changed.

# --- Creating a tuple ---
# Tuples use parentheses ().
marks = (98, 99, 33, 12)
print(marks)
print(type(marks))        # <class 'tuple'>

# A tuple can store different data types.
# This tuple represents a server: name, IP address, and port.
server_info = ("web-01", "192.168.1.10", 8080)

# --- Indexing ---
# Indexing works the same as lists: the first item has index 0.
print(server_info[0])     # web-01
print(server_info[1])     # 192.168.1.10

# --- Negative indexing ---
print(server_info[-1])    # last item -> 8080
print(server_info[-2])    # second last item -> 192.168.1.10

# --- Slicing ---
# Slicing works the same as lists: tuple[start:stop], stop is excluded.
print(marks[1:3])         # (99, 33)
print(marks[:2])          # (98, 99)

# --- len() ---
print(len(server_info))   # 3 items

# --- IMMUTABILITY ---
# Tuples cannot be changed after creation.
# The line below is NOT allowed and would raise a TypeError:
# server_info[0] = "web-02"

# --- Membership (in) ---
print("web-01" in server_info)    # True
print("db-01" in server_info)     # False

# --- Loop through a tuple ---
for item in server_info:
    print(item)

# --- Tuple unpacking ---
# We can assign each tuple value to a variable in one line.
# The number of variables must match the number of items.
name, ip_address, port = server_info
print(name)               # web-01
print(ip_address)         # 192.168.1.10
print(port)               # 8080