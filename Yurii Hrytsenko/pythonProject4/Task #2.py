while True:
    info = input("Enter your name and age using whitespace:\n").lower().strip()

    if info == "quit":
        break

    name, age = info.split()

    if not age.isdigit() or not name.isalpha():
        print("Invalid enter try again!")
        continue
    else:
        age = int(age)
        name = name.title()

    message = f"Hello {name}, on your next birthday you'll be {age+1} years!"

    print(message)
