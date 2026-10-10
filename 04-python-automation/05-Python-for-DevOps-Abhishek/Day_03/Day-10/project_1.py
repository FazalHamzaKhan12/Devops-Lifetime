import os

# number = input("Please provide a number : ")
# print(number)


folders = input("Please provide list of folders names with spaces b/w : ").split()
# print(folders)
# print(type(folders)) # List

for folder in folders:
    # print(folder)
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("\n" + folder, "file not Found")
        continue

    except PermissionError:
        # you can use this when you have linux system 
        print(": " + folder)

    print("-------- Listing Files for the folder - " + folder)
    # print(files)
    for file in files:
        print(file)
    