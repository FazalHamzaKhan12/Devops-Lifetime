# WAF to count the number of vowels in a string

x = input("Enter a string: ")

vowels = {"a", "e", "i", "o", "u"}


def vowel_counting(x):
    count = 0

    for character in x:
        if character in vowels:
            count += 1

    print(f"Number of vowels: {count}")


vowel_counting(x)