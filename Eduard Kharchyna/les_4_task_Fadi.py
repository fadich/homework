month = input("please enter in lowercase the full name or number of the month of your birth: ")
winter = ("december", "january", "february", "1", "2", "12")
spring = ("march", "april", "may", "3", "4", "5")
summer = ("june", "july", "august", "6", "7", "8")
autumn = ("september", "october", "november", "9", "10", "11")
season = ""
if month in winter:
    season = "winter"
elif month in spring:
    season = "spring"
elif month in summer:
    season = "summer"
elif month in autumn:
    season = "autumn"
print(f"You were born in {season}.")
