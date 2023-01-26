# LESSON_3

# Task 1: The greeting program.
from datetime import datetime

day = datetime.now().strftime('%A')
name = 'arina'.title()

# 1st version of formatting
print(f'Good day {name}! {day} is a perfect day to learn some python')

# 2nd version of formatting
print('Good day {0}! {1} is a perfect day to learn some python'.format(name, day))


# Task 2: Manipulate strings.
first_name = 'arina'.title()
last_name = 'trofimenko'.title()

print('Good day', first_name + ' ' + last_name + '!', day, 'is a perfect day to learn some python')

# 2nd version with string formatting
print('Good day {}! {} is a perfect day to learn some python'.format(first_name + ' ' + last_name, day))


# Task 3: Using python as a calculator.

a = int(input('Enter a:\n'))
b = int(input('Enter b:\n'))
if b != 0:
    print('Subtraction: ' + str(a - b),
          'Addition: ' + str(a + b),
          'Division: ' + str(round(a / b, 1)),
          'Multiplication: ' + str(a * b),
          'Modulus: ' + str(a % b),
          'Exponent: ' + str(a ** b),
          'Floor division: ' + str(a // b),
          sep='\n')
else:
    print('Subtraction: ' + str(a - b),
          'Addition: ' + str(a + b),
          'Division: Error',
          'Modulus: Error',
          'Multiplication: ' + str(a * b),
          'Exponent: ' + str(a ** b),
          'Floor division: Error',
          sep='\n')



