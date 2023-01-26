# Task 1: The Guessing Game.
import random

random_number = random.randint(1, 10)

while True:
    # you can make this helper 'print' active to know random number for checking code
    # print(f'helper: {random_number}')
    try:
        guess_number = int(input('Please enter you number from 1-10: '))
    except (ValueError, TypeError):  # Check when entering non-integer numbers or letters
        print('You must enter only integer. ')
        continue
    if not (0 < guess_number < 11):
        continue
    elif guess_number != random_number:
        print(f'Unfortunately, you were wrong. Random number was: {random_number}.\n'
              f'Let\'s try one more time?')
        random_number = random.randint(1, 10)
    else:
        print('Congratulations! You\'re right!')
        break


# Task 2: The birthday greeting program.
input_message = 'Enter your NAME and AGE,separated by a space: '
while True:
    try:
        name, age = input(input_message).split()
    except (ValueError, TypeError):
        input_message = 'Please, use a SPACE between NAME and AGE!\nEnter your NAME and AGE again: '
        continue
    print(f'Hello dear {name.title()}, on your next birthday you’ll be {int(age)+1} years! 🐣')
    break


# Task 3: Words combination
import random

word = 'hello'
len_word = len(word)

for _ in range(5):
    # get 5 random strings of length "len_word" without repeating letters
    random_words = ''.join(random.sample(word, len_word))
    print(random_words)
