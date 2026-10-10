# Python Day 2

Day 2 of my Python learning journey — operators and conditional statements.

## Topics Covered

- Operator precedence
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical operators: `and`, `or`, `not`
- Conditional statements: `if`, `elif`, `else`
- `range()` basics

## Practice

The `practice/` folder contains one program:

- `01_simple_calculator.py` — a simple calculator built with `if` / `elif` / `else`

## What I Learned

- Comparison operators return a boolean result: `True` or `False`.
- Logical operators combine multiple conditions into one boolean value.
- `if` / `elif` / `else` decides which block of code runs.
- Operator precedence controls the order of evaluation; parentheses override it.
- `range()` generates sequences of numbers — the foundation for loops in Day 3.

## DevOps Connection

Conditions are the backbone of automation decisions. Later, scripts will use
checks such as `if disk_usage > 80:` to decide whether to act, and `range()`
makes it possible to repeat actions a fixed number of times as I move on to loops.