# Task 1

name = input("Enter your name: \n")
day = input("Enter current day: \n")

name = name.title()
day = day.title()

print(f"Good day {name}! {day} is a perfect day to learn some python.")
print("Good day {}! {} is a perfect day to learn some python.".format(name, day))
print("Good day " + name + "! " + day +
     " is a perfect day to learn some python.\n\n")

# Task 2

first_name = input("Enter your first name: \n")
last_name = input("Enter your last name: \n")

name = first_name.title() + " " + last_name.title()

print(f"Hello, {name}!")

