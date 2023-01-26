# Additional Task
number_of_month = ('12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')
name_of_month = ('december', 'january', 'february', 'march', 'april', 'may',
                 'june', 'july', 'august', 'september', 'october', 'november')

while True:
    month = input('Please enter number (from 1 to 12) OR name of month: ').lower()
    if month in number_of_month[0:3] or month in name_of_month[0:3]:
        print('The season is WINTER')
        break
    elif month in number_of_month[3:6] or month in name_of_month[3:6]:
        print('The season is SPRING')
        break
    elif month in number_of_month[6:9] or month in name_of_month[6:9]:
        print('The season is SUMMER')
        break
    elif month in number_of_month[9:] or month in name_of_month[9:]:
        print('The season is FALL')
        break


# Task 1: String manipulation
hello_str = 'helloworld'
created_str = hello_str[:2] + hello_str[-2:]

if len(hello_str) < 2:
    print("")
else:
    print(f'Result: {created_str}')


 # Task 2: The valid phone number program.
while True:
    phone_num = input('Enter your phone number: ')

    if len(phone_num) != 10:
        print('Phone Number must be 10 characters long.')
    elif not phone_num.isdigit():
        print('Phone Number must contain only numerical characters.')
    else:
        print(f'Phone Number: {phone_num} is valid. Thank you!')
        break


# Task 3: The math quiz program.
answer = str(5)
while True:
    mathematical_expression = input('55/11 = ')
    if mathematical_expression != answer:
        print('Wrong answer. Try one more time!')
    else:
        print('Congratulations! The answer is correct.')
        break


# Task 4: The name check.
name = 'arina'
input_name = input('Enter your name: ').lower()
if input_name == name:
    print(f'{input_name == name}: input name is equal to the stored name')
else:
    print('Input name isn\'t equal to the stored name')
