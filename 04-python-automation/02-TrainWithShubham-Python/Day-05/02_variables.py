# variables , data types, and operators

environment = "staging"
cpu_cores = 4
load_average = 0.75
is_active = True

print("\nEnvironment:", environment, "->", type(environment))
print("CPU Cores:", cpu_cores, "->", type(cpu_cores))
print("Load Average:", load_average, "->", type(load_average))
print("Is Active:", is_active, "->", type(is_active))


a = 100
b = 300
print("\nAddition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor division :", a // b)
print("Remainder      :", a % b)


# input() always gives you a str, so cast when you need a number

disk_used_str = "32"
disk_used = int(disk_used_str)
print("\nDisk Used:", disk_used, "->", type(disk_used))