# Task 3

print('''
Enter your expression to calculator using spaces. (a + b)
Use actions to:
    + to Addition,
    - to Subtraction,
    * to Multiplication,
    / to Division,
    // to Floor Division,
    ** to Exponent(Power),
    abs to Modulus(a abs).
Enter "quit" to Exit.
''')

actions_list = ["+", "-", "*", "/", "//", "**", "abs"]
flag = True

while flag:
    expression = input("Enter your expression: \n")

    if expression == "quit":
        flag = False
        break

    operands = expression.split()

    action = operands[1]
    first_number = int(operands[0])
    second_number = int(operands[2])

    if action not in actions_list:
        print("There is no such action! Try again!")
        continue

    if action == '+':
        print(first_number + second_number)

    if action == '-':
        print(first_number - second_number)

    if action == '*':
        print(first_number * second_number)

    if action == '/':
        if second_number != 0:
            print(first_number / second_number)
        else:
            print("You can`t divide by zero! Try again!")

    if action == '/':
        if second_number != 0:
            print(first_number / second_number)
        else:
            print("You can`t divide by zero! Try again!")

    if action == '**':
        print(first_number ** second_number)

    if action == 'abs':
        if first_number <= 0:
            print(first_number * -1)
        else:
            print(first_number)