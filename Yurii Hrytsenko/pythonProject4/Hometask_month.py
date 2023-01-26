winter = ["december", "january", "february"]
spring = ["march", "april", "may"]
summer = ["june", "july", "august"]
autumn = ["september", "october", "november"]

seasons = winter + spring + summer + autumn

while True:
    month = input(
        "Enter the month of your birthday " +
        "(you can use number or name of month):\n"
    ).lower().strip()

    if month == "quit":
        break

    if not month.isdigit():
        print("Invalid enter, try again!")

    if month.isdigit():
        if int(month) <= 0 or int(month) > 12:
            print("There is no such number of month, try again")
        elif int(month) == 1 or int(month) == 2 or int(month) == 12:
            print("You born in winter!")
        elif 3 <= int(month) <= 5:
            print("You born in spring!")
        elif 6 <= int(month) <= 8:
            print("You born in summer!")
        elif 9 <= int(month) <= 11:
            print("You born in autumn!")

    if month in seasons:
        if month in winter:
            print("You born in winter!")
        elif month in spring:
            print("You born in spring!")
        elif month in summer:
            print("You born in summer!")
        elif month in autumn:
            print("You born in autumn!")
        else:
            print("There is no such mont, try again")
