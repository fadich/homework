import random
user_string = input("Hello. Please input a string: ")
user_string_list = list(user_string)
number_of_combination = 5
while number_of_combination > 0:
    random.shuffle(user_string_list)
    user_string = "".join(user_string_list)
    print(user_string)
    number_of_combination -=1