# Apna College - Python Fundamentals

A hands-on foundation in core Python programming syntax, operators, data structures, and functions to prepare for systems and DevOps automation.

## About This Course

- **Course:** Apna College Python Full Course
- **Source:** [Apna College YouTube Channel](https://www.youtube.com/@ApnaCollegeOfficial)
- **Focus:** Python syntax, data types, conditional branching, loops, built-in collections, and modular functions.
- **Why It Is Useful:** Coming with prior programming experience in C++ and C#, this course provided a rapid way to map core programming logic to idiomatic Python syntax without unnecessary complexity.
- **Where It Fits in the DevOps Journey:** Before writing automated deployment or infrastructure scripts, a solid grasp of Python data types, dictionaries, lists, and function boundaries is essential. This is Step 01 in the learning path.

## Topics Covered

| Status | Topic | Details |
|---|---|---|
| ✅ | Print & Comments | Output strings, single-line comments (`#`) |
| ✅ | Variables & Data Types | `str`, `int`, `float`, `bool`, `type()` checking |
| ✅ | Type Conversion | Casting between strings, integers, and floats |
| ✅ | String Manipulation | Methods: `.upper()`, `.lower()`, `.find()`, `.replace()`, slicing |
| ✅ | Arithmetic & Assignment Operators | `+`, `-`, `*`, `/`, `//`, `%`, `**`, `+=`, `-=` |
| ✅ | Comparison & Logical Operators | `==`, `!=`, `<`, `>`, `<=`, `>=`, `and`, `or`, `not` |
| ✅ | Conditional Statements | `if`, `elif`, `else` decision trees |
| ✅ | Ranges & Iteration | `range()` generator, `for` loops, `while` loops |
| ✅ | Lists | Indexing, slicing, `.append()`, `.insert()`, `.remove()`, `.pop()` |
| ✅ | Tuples | Fixed sequences, immutability, tuple unpacking |
| ✅ | Sets | Unique elements, removing duplicates, set operations |
| ✅ | Dictionaries | Key-value pairs, `.keys()`, `.values()`, `.items()`, `.get()` |
| ✅ | Functions | User-defined (`def`), parameters, return values, built-in functions |
| ✅ | Modules & Standard Library | `math`, `random` modules |
| ✅ | Mini-Projects & Practice | Number guessing game, calculators, validation scripts |

## Practical Examples

| Script | Purpose | Python Concept | Why It Is Useful |
|---|---|---|---|
| [01_sum_calculator.py](Day-01/practice/01_sum_calculator.py) | Reads two numbers and computes their sum | `input()`, `int()` casting, arithmetic | Foundation for taking interactive CLI inputs |
| [02_bill_calculator.py](Day-01/practice/02_bill_calculator.py) | Calculates total expenses and item averages | Arithmetic operators, variables | Basic arithmetic for computing metric totals and averages |
| [01_simple_calculator.py](Day-02/practice/01_simple_calculator.py) | Interactive multi-operation calculator | `if` / `elif` / `else` control flow | Essential branching logic for automation decision-making |
| [15_loops.py](Day-03/15_loops.py) | Iteration over sequences and numbers | `for`, `while`, `break`, `continue` | Repeating tasks across servers, files, or log lines |
| [19_dictionary.py](Day-03/19_dictionary.py) | Structured key-value storage and access | Dictionaries, `.items()`, `.get()` | Parsing configuration files and JSON API responses |
| [23_mini-project-guessing_number.py](Day-04/23_mini-project-guessing_number.py) | Interactive guessing game with random numbers | `random` module, `while` loop, conditionals | Combining control flow, random states, and user interaction |
| [03_prime-number_find_function.py](Day-04/practice/03_prime-number_find_function.py) | Checks prime numbers efficiently | Functions, loops, modulus operator | Reusable algorithmic function design |

## Python Concepts Learned

- **Variables & Dynamic Typing:** Python does not require explicit type declarations; variables adapt dynamically to the assigned values.
- **Type Casting:** Input from `input()` is always a string; explicit conversion via `int()` or `float()` is necessary for calculations.
- **Collections:**
  - **Lists:** Ordered, mutable arrays used for collections of items.
  - **Tuples:** Ordered, immutable records that safeguard against accidental changes.
  - **Sets:** Unordered collections that enforce uniqueness.
  - **Dictionaries:** Key-value pairs allowing fast lookup by key.
- **Control Flow:** Indentation-based block scoping with `if`/`elif`/`else` statements and loops.
- **Functions:** Reusable blocks declared with `def` that accept arguments and return values.

## DevOps Relevance

- **Lists:** Store lists of target hostnames, IP addresses, Kubernetes pods, or container IDs.
- **Dictionaries:** Model JSON/YAML server definitions, cloud metadata, and API payloads.
- **Sets:** Extract unique error codes or unique IP addresses from access log streams.
- **Conditionals:** Implement threshold checks (e.g., alert if disk usage > 85%).
- **Loops:** Iterate over server inventories to execute commands or check health.
- **Functions:** Modularize automation scripts into testable units (e.g., `check_status()`, `restart_service()`).

## Learning Notes

- `input()` in Python 3 always captures user input as a string (`str`), so forgetting to cast with `int()` or `float()` leads to `TypeError`.
- Dictionaries raise a `KeyError` if accessed with square brackets for a non-existent key; using `.get("key", default)` prevents script termination.
- Tuples cannot be modified after creation; use lists when items need to be appended or changed.

## Projects / Exercises

### Day 01 — Basics & Operations
- [Lesson Notes & Overview](Day-01/README.md)
- [01_sum_calculator.py](Day-01/practice/01_sum_calculator.py)
- [02_bill_calculator.py](Day-01/practice/02_bill_calculator.py)
- [03_personal_info.py](Day-01/practice/03_personal_info.py)

### Day 02 — Operators & Conditions
- [Lesson Notes & Overview](Day-02/README.md)
- [01_simple_calculator.py](Day-02/practice/01_simple_calculator.py)

### Day 03 — Loops & Collections
- [Lesson Notes & Overview](Day-03/README.md)
- [01_practice_loops.py](Day-03/practice/01_practice_loops.py)
- [02_practice_lists_tuples_sets.py](Day-03/practice/02_practice_lists_tuples_sets.py)

### Day 04 — Functions & Mini-Project
- [Lesson Notes & Overview](Day-04/README.md)
- [23_mini-project-guessing_number.py](Day-04/23_mini-project-guessing_number.py)
- [01_if-else_function_practice.py](Day-04/practice/01_if-else_function_practice.py)
- [02_vowels-in_string_function_practice.py](Day-04/practice/02_vowels-in_string_function_practice.py)
- [03_prime-number_find_function.py](Day-04/practice/03_prime-number_find_function.py)
- [04_average_marks_function.py](Day-04/practice/04_average_marks_function.py)

## What I Learned

Mastered the fundamental syntax of Python, including dynamic typing, built-in string methods, collection data structures, and functional modularity. Built the muscle memory needed to write error-free basic scripts.

## Next Step

Progress to [02-TrainWithShubham-Python](../02-TrainWithShubham-Python/README.md) to apply Python to system metrics (`psutil`), REST API handling (`requests`), web services (`fastapi`), and basic AWS operations (`boto3`).