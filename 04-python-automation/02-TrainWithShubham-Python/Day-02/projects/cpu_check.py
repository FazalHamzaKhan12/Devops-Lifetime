cpu = int(input("Enter the CPU usage percentage: "))
print(f"The CPU usage is: {cpu}%")

if cpu > 50:
    print("The CPU is overloaded.")
elif cpu > 20 and cpu <= 50:
    print("The CPU is moderately utilized.")
else:
    print("The CPU is underutilized.")
