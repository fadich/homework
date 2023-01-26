# Homework Fadi

print('\nGet your season of birth\n')
month = input('Please, type the month you were born (use numbers 1 to 12):\n')
while True:
    if month.isdigit() == False:
        month = input('Wrong format. Please, use numerical: \n')
    elif 1 > int(month) or int(month) > 12:
        month = input('The entered number is not a month. Please, enter 1 to 12: \n')
    else:
        if int(month) == 12 or 1 <= int(month) <= 2:
            print('Ви народилися взимку')
        elif 3<= int(month) <= 5:
            print('Ви народилися навесні')
        elif 6 <= int(month) <= 8:
            print('Ви народилися влітку')
        else:
            print('Ви народилися восени')
        break

# Homework LMS
# ex1

print('\nTwo first and two last symbols in a string\n')
original_string = input('Type your string here:\n')
if len(original_string) > 2:
    processed_string = original_string[0:2] + original_string[-2:]
else:
    processed_string = 'Empty string'
print(processed_string)

# ex2

print('\nGuessing if the phone number is correct\n')
phone_number = input('Type in your phone number:\n')
if phone_number.isdigit() == True:
    if len(phone_number) == 10:
        print('This might be a phone number. '
              'We should have checked the country code, though')
    else:
        print('Bummer! Not a phone number :( '
              'Too many digits for a phone number')
else:
    print('If you considered calling this number, don\'t: '
          'other symbols than digits used; this is definitely '
          'not a phone number')

#ex3
from random import randint
'''Цю штуку писати було весело, але оцим "here's your score" у кінці
я намагалася відволікти увагу від того, що тут пропонується тільки одна
арифметична дія. Але я не впевнена, як копактніше можна написати
випадково згенерований математичний вираз, щоб і арифметична операція
була обрана випадковим чином
'''

print('\nTask with calculations\n')
answer = ''
variable_a = 0
variable_b = 0
correct = 0
incorrect = 0
invalid = 0
while True:
    variable_a = randint(0, 100)
    variable_b = randint(0, 100)
    print(f'{variable_a} + {variable_b}')
    answer = input('Please, enter your answer.\n'
                   'If you want to exit, please, type "e" or "E":\n')
    if answer.lower() != 'e':
        if answer.isdigit():
            if variable_a + variable_b == int(answer):
                correct += 1
                print('Great job! Correct')
            else:
                incorrect += 1
                print('Oh no, you got it all wrong... '
                      'Let\'s try again.')
        else:
            invalid += 1
            print('Oh, what is this? Not digits? Can\'t accept that... '
                  'Please, try answering again. Remember, '
                  'if you want to exit, type "e" or "E"')
    else:
        print(f'Bye! It was cool. Here\'s your score:\n'
              f'Correct answers: {correct}\n'
              f'Incorrect answers: {incorrect}\n'
              f'Invalid answers: {invalid}')
        break

# ex4
'''Я прописала це у вигляді циклу, у якому варіант виходу з нього тільки один.
Мені просто згадався Румпельштільцхен. Не думаю, що цей код корисний чи раціональний.
Але прописати його циклом, коли в умові цього нема, здавалося цікавим.
Щоб це був не цикл, я би замінила while на if і прибрала би 
переписування змінної через інпут у разі помилки
'''

print('\nA name guessing cycle\n')
true_name = 'oleksandra'
name_given = input('Please, enter my name:\n')
while name_given.lower() != true_name:
    print('That\'s not my name:( Wanna try again?')
    name_given = input('You will try endlessly, until you guess my name. Ha-ha.\n')
else:
    print('Wow, correct! I set you free')



