# Collection Data Types: list, tuple, set, dict

# Dictionary: It is a collection of key-value pairs. It is unordered, mutable, and indexed. Dictionaries are defined using curly braces {}.

info = {
    "name": "Shubham",
    "year": 2024,
    "env": "Python"
}

print(info)  # Output: {'name': 'Shubham', 'year': 2024, 'env': 'Python'}
print(info["name"])  # Output: Shubham
print(info["year"])  # Output: 2024


# List: It is a collection of ordered, mutable, and indexed elements. Lists are defined using square brackets [].
list = [1, 2, 3, 4, 5]
print(list)  # Output: [1, 2, 3, 4, 5]


# Tuple: It is a collection of ordered, immutable, and indexed elements. Tuples are defined using parentheses ().
tuple = (1, 2, 3, 4, 5)
day_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(day_of_week)  # Output: ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(day_of_week[0])  # Output: Monday



# Set: It is a collection of unordered, mutable, and unindexed elements. Sets are defined using curly braces {}.
marks = {98, 33, 95, 1, 98}  # 98 appears twice
print(marks)  # Output: {1, 33, 95, 98}  # 98 appears only once
