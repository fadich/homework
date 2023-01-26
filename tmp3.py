import random


operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "**": lambda x, y: x ** y,
    "/": lambda x, y: x / y,
    "//": lambda x, y: x // y,
    "%": lambda x, y: x % y,
}

a = random.randint(0, 100)
b = random.randint(1, 100)  # from 1 - just not to divide by zero!

op_key = random.choice(list(operations.keys()))

print(
    f"{a} {op_key} {b} = {operations[op_key](a, b)}"
)
