# Calculator V2
from actions import action
from validation import validation

flag = True
result = 0

instruction = """
Enter your expression with using spaces. Sample: (a x b)
You can:
+ to Addiction;
- to Subtraction;
* to Multiplication;
/ to Division;
** to Power;
// to Floor division;
abs to Modulus. Sample (abs a)
Enter "inst" to show instruction.
Enter "quit" to exit.
"""
print(instruction)

while flag:

    expression = input("Enter your expression:\n").lower().strip()

    if expression == "quit":
        print("Goodbye")
        flag = False
        break

    if expression == "inst":
        print(instruction)

    if not validation(expression):
        print("Invalid enter!")
        continue

    operands = expression.split()

    a = 0
    b = 0
    c = 0

    length = len(operands)

    if length == 0:
        print("")
        continue
    elif length == 1:
        print(float(operands[0]))
        continue
    elif length == 2:
        a = float(operands[1])
        c = operands[0]
    elif length == 3:
        a = float(operands[0])
        b = float(operands[2])
        c = operands[1]
    else:
        print("Invalid enter")

    result = action(a, b, c)

    print(result)
