# Task 4
flag = True
name = "yurii"

while flag:
    name_test = input("Enter name: \n").lower().strip()

    if name_test == "quit":
        flag = False
        break

    if name == name_test:
        print("Correct!")
    else:
        print("Incorrect!")