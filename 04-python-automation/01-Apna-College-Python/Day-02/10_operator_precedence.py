# Operator precedence is the order in which Python
# evaluates operators inside an expression.

# From highest to lowest, some common ones are:
# Parentheses ()
# Exponentiation **
# Multiplication / Division / Floor Division / Modulus
# Addition / Subtraction

# Multiplication has higher precedence than addition.
result = 2 + 3 * 4
print(result)  # 14, because 3 * 4 is calculated first.

# Parentheses change the order of evaluation.
result = (2 + 3) * 4
print(result)  # 20, because (2 + 3) is calculated first.

# Exponentiation is evaluated before multiplication.
result = 2 + 3 ** 2
print(result)  # 11, because 3 ** 2 = 9, then 2 + 9.

# Multiplication and division are done from left to right.
result = 20 / 2 * 5
print(result)  # 50.0, because (20 / 2) = 10, then 10 * 5.