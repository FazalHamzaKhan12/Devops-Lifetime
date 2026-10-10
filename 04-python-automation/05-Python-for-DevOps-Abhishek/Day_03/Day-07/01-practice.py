import sys

type = sys.argv[1]

if type == "t2.micro":
    print("this will charge 3 dollor par day ")
elif type == "t2.medium":
    print("this will charge 7 dollor par day ")
elif type == "t2.large":
    print("this will charge 7 dollor par day ")
else:
    print("mismathc")