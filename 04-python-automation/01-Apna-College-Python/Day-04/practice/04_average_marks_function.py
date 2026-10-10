def average_marks(marks):
    total = 0

    for mark in marks:
        total += mark

    return total / len(marks)


marks = [80, 70, 90, 60]

average = average_marks(marks)

print(f"Average marks: {average}")