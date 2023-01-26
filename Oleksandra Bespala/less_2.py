#ex1
name = "Oleksandra"
day = "Monday"
print(f"Good day, {name}, {day} is a perfect day to learn some python!")

string_to_format = "Good day, {}, {} is a perfect day to learn some python!"
print(string_to_format.format(name, day))

print("Good day, %s, %s is a perfect day to learn some python!"%(name, day))

#ex2
name = "name"
surname = "surname"
full_name = name.title() + " " + surname.title()
print("Welcome to your life, " + full_name)

#ex3
a = 32
b = 13

print(a + b)
print(a - b)
print(a / b)
print(a * b)
print(a ** b)
print(a % b)
print(a // b)
