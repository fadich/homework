''''''
user_string = input("Please input string: ")
if len(user_string) >= 2:
    print(user_string[:2] + user_string[-2:])
else:
    print("")
