def add_numbers(num1, num2):
    return num1 + num2
weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# def take_backu
def take_backup(day):
    if day == "Sunday":
        print("Taking backup on Sunday")
    else:
        print(f"No backup today {day}")

if __name__ == "__main__":
    total = add_numbers(10, 20)
    print(f"The total is {total}")

    for day in weeks:
        take_backup(day)