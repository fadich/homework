#Task1
name = 'cloudysky'
if (len(name)) >= 2:
    print(name[0:2] + name[-2:]) #Якщо 2 або більше символи - друкує перші 2 та останні 2 літери
elif (len(name)) < 2:
    print(' ')                   #Якщо менше 2х літер - нічого не друкує

print('\n')

#Task2

#Перевіряємо, чи є у змінній літери
number = '0983420130'
if number.isdigit():
    print('contains only numbers')
else:
    print('contains not only numbers')

#Перевіряємо, cкільки символів у рядку
long = '1732449910'
if len(long)  >= 11:
    print('false')
elif len(long) <= 10:
    print("true")

print('\n')

#Task3

#Перевіряємо правильність математичного виразу
number = 10
number1 = 12
expression = number + number1
print(f'result = {expression}')
if expression <= 15:
    print('false')
elif expression > 22:
    print('true')
elif expression > 21:
    print('good answer')
else:
    print('error')

print('\n')

#Task4
name = 'Andrii'
name1 = 'andriI'
if name.lower() == name1.lower() :    #Andrii == andriI
    print('all good')
else:
    print('that is not good')

print('\n')

#Task5

#I was born in December
month = 12
if(month <= 2 or month == 12):     #1й, 2й та 12й місяці
    print("I was born in winter")
elif(month >= 3 and month <=5 ):   #3й, 4й та 5й місяці
    print('I was born in spring')
elif(month >=6 and month <=8):     #6й, 7й та 8й місяці
    print("I was born in summer")
elif(month >=9 and month <=11 ):   #9й, 10й та 11й місяці
    print("I was born in autumn")



