# Python Day 1

My very first day of learning Python — the absolute fundamentals of the language.

## Topics Covered

- Printing output with `print()`
- Variables and variable naming rules
- Data types: `str`, `int`, `float`, `bool` (checked with `type()`)
- User input with `input()`
- Comments (`#`)
- Type conversion / casting with `int()`, `float()`, `str()`
- Strings and concatenation (`+`)
- String operations: `.upper()`, `.lower()`, `.capitalize()`, `.find()`, `.replace()`, `in`, `.startswith()`
- Arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Assignment operators: `=`, `+=`, `-=`, `*=`, `/=`

## Practice

The `practice/` folder contains three small programs based on these basics:

- `01_sum_calculator.py` — adds two numbers entered by the user
- `02_bill_calculator.py` — adds fruit prices and finds the average price
- `03_personal_info.py` — takes a user's name and prints their details

## What I Learned

- `print()` is the simplest way to show output; `input()` always returns a string.
- Every value has a type (`str`, `int`, `float`, `bool`) and `type()` shows it.
- Strings can be joined with `+` and have useful built-in methods.
- Numbers from `input()` must be converted with `int()` / `float()` before doing math.
- Operators calculate values, and shortcuts like `+=` update variables in place.

## DevOps Connection

These fundamentals are the building blocks for automation later:

- Variables can store server names, IP addresses, ports, and status flags.
- `input()` is the start of interactive setup scripts.
- Type conversion matters when parsing numbers from configs or logs.
- Operators are used for totals, averages, capacity math, and counters.