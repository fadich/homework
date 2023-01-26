# homework Fadi
# 1
n = int(input('Any number:\n'))
a = 1
factorial = 1

while a <= n:
    factorial = factorial * a
    a += 1
print(factorial)

# 2

n = int(input('Print "n":\n'))
a = int(input('Print "a":\n'))
b = int(input('Print "b":\n'))
number = 0

while number <= n:
    number += 1
    if number % a == 0 and number % b == 0:
        print(f'Бінго! Число {number} ділиться як на {a}, так і на {b}!')
        break
    elif number % b == 0:
        print(f'Число {number} кратне {b}!')
    elif number % a == 0:
        print(f'Число {number} кратне {a}!')

# ex1
'''В умові не йшлося про цикли, умова загалом проста.
    Тому я не мудрувала з рішенням, не включала цикли
    і валідацію інпута
    Але по хорошому перед переводом в інт треба перевірити,
    чи в інпуті тільки цифри, бо якщо там буде символ чи буква,
    еррор зламає все на початку
    + імпортувала рандом модуль один раз на всі вправи, оскільки один файл
'''

import random

print('The Guessing Game\n')

entered_number = int(input('Please, guess a number 1 to 10:\n'))
generated_number = random.randint(1,10)
if 1 <= entered_number <= 10:
    print(f'Your number is {entered_number}, random number is {generated_number}')
else:
    print('Your number is not in range')

# ex2

print('The Birthday Greeting Program\n')

name = input('Please, enter your name:\n')
age = int(input('Please, enter your age:\n')) + 1
print(f'Hi {name}, next year you\'ll be {age}')

# ex3

print('Words combination\n')

string = 'hello'
random_string = ''
i = 0

for i in range(5):
    random_string = ''.join(random.sample(string, 5))
    print(random_string)