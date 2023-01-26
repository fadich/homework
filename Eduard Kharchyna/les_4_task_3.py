print("Hi. This is a little program to test your addition skills, subtract, multiply and divide.")
number_1 = int(input("Please enter the first integer: "))
number_2 = int(input("Please enter the second integer: "))
sum_1 = number_1 + number_2
result_sum = int(input("Write the sum of the numbers you entered: "))
if sum_1 == result_sum:
    print("Great! You have made the correct calculations.")
else:
    print("You have made a mistake. The correct answer is:", sum_1)
remainder = number_1 - number_2
result_remainder = int(input("Write the remainder of the numbers you entered: "))
if remainder == result_remainder:
    print("Great! You have made the correct calculations.")
else:
    print("You have made a mistake. The correct answer is:", remainder)
product = number_1 * number_2
result_product = int(input("Write the product of the numbers you entered: "))
if product == result_product:
    print("Great! You have made the correct calculations.")
else:
    print("You have made a mistake. The correct answer is: ", product)
if number_2 == 0:
    print("Now it\'s time to divide. As you know, you can\'t divide by zero.\
    You wrote 0 as the divisor.")
    number_2 = int(input("Enter another number: "))
    if number_2 == 0:
        print("Well, you can\'t divide by zero. So let the second number be 7.")
        number_2 = 7
quotient = number_1 / number_2
result_quotient = int(input("Write the quotient of the numbers you entered: "))
if quotient == result_quotient:
    print("Great! You have made the correct calculations.")
else:
    print("You have made a mistake. The correct answer is: ", quotient)
print("Thank you for your attention.")
