# Task 1
sample_str = 'Beetroot'
if len(sample_str) >= 2:
    new_str = sample_str[:2] + sample_str[-2:]
    print(new_str)
else:
    new_str = ''
    print(new_str)
# Task 2
phone_num = '133556578643'
length = len(phone_num)
if phone_num.isnumeric() and length == 10:
    print('Right format')
else:
    print('Wrong format')
# Task 3
print('What is the answer for 2*2*2*100-9?')
answer = input('Your answer >> ')
if answer == str(2*2*2*100-9):
    print('Yeah buddy')
else:
    print('Holy crap. You should improve your Math!')
# Task 4
name = 'mykhailo prusov'
ask_name = input('GIVE ME YOUR MONEY... AHH NO. NOT MONEY. GIVE ME YOUR NAME!!')
if ask_name.lower() == name:
    print(True,'That\'s correct,mate')
else:
    print(False,'Man... You are wrong')


