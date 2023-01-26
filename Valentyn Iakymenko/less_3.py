s = "Today" #task1
print(len(s))
print(s[:2] + s[-2:])

number = "0733217295" #task2
if(len(number) > 10):
    print("Too much numbers") #пише повідомлення, якщо у номера забагато цифр
if(len(number) < 10):
    print("Not enough numbers") #пише повідомлення, якщо у номера бракує цифр
elif number.isdigit():
    print("Number is correct") #якщо номер вірний
else:
    print("should contains only numbers") #якщо у номера присутні букви



number1 = 10 #task3
number2 = 12
expression = number1 + number2
print(f'result = {expression}')
if expression == '22':
    print('error')
elif expression == '22':
    print('false')
else:
    print('true')

name="anton"       #task4
if [name >= "A" and name <= "Z"]: #множина усіх літер з верхнього регістру
    print(name + " " +"true");
elif [name >="a" and name <="z"]: #множина усіх літер з нижнього регістру
        print(name+" "+ "true")

month=12  #task5
if(month <= 2):
    print("Ви народились зимою");
if(month > 12):
        print("Перевірте місяць")
elif(month <=5):
    print("Ви народился весною");
elif(month >=9 and month <=11 ):
    print("Ви народилися восени");
elif(month >=6 and month <=8):
    print("Ви народилися влітку");
else:
    print("Ви народились зимою")








