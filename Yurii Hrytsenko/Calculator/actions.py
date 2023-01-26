
def action(a, b, c):
    if c == "+":
        return addition(a, b)
    elif c == "-":
        return subtraction(a, b)
    elif c == "*":
        return multiplication(a, b)
    elif c == "/":
        return division(a, b)
    elif c == "**":
        return power(a, b)
    elif c == "//":
        return floor_division(a, b)
    elif c == "abs":
        return modulus(a)


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "You can`t division by zero!!!"


def floor_division(a, b):
    if b != 0:
        return a // b
    else:
        return "You can`t division by zero!!!"


def power(a, b):
    return a ** b


def modulus(a):
    if a >= 0:
        return a
    else:
        return -a
