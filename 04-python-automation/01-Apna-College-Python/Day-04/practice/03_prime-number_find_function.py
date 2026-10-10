# WAF to print if a number is prime or not

x = int(input("Enter the number to check if it is prime or not: "))


def prime_find(x):
    if x <= 1:
        print("It is not a prime number")
        return

    for i in range(2, x):
        if x % i == 0:
            print("It is not a prime number")
            return

    print("It is a prime number")


prime_find(x)