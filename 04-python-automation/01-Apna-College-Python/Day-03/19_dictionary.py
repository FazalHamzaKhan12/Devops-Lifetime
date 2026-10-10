# A dictionary stores data as KEY-VALUE pairs.
# Each key is unique and is connected to one value.

# --- Creating a dictionary ---
# Dictionaries use curly braces {} with key: value pairs.
server = {
    "name": "web-01",
    "ip": "192.168.1.10",
    "status": "running",
    "port": 8080
}

print(server)

# --- Accessing values ---
# We access a value by its key.
print(server["name"])     # web-01
print(server["ip"])       # 192.168.1.10
print(server["port"])     # 8080

# --- Adding values ---
server["region"] = "us-east-1"    # add a new key-value pair
print(server)

# --- Updating values ---
server["status"] = "stopped"      # change the value of an existing key
print(server)

# --- Removing values ---
del server["port"]                # remove a key-value pair
print(server)

# --- keys(), values(), items() ---
print(server.keys())      # all keys
print(server.values())    # all values
print(server.items())     # all key-value pairs

# --- Membership (in) ---
# in checks the KEYS by default.
print("name" in server)              # True
print("192.168.1.10" in server)      # False (it is a value, not a key)

# --- Loop through a dictionary ---
for key in server:
    print(key, server[key])

# Loop with items() to get each key-value pair directly.
for key, value in server.items():
    print(key, value)