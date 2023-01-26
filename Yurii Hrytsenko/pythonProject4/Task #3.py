import random

str_ = input("Enter your string:\n")

letter_list = [char for char in str_]

new_list = []

while len(new_list) < 6:
    new_str = random.sample(letter_list, len(letter_list))
    new_word = ""
    for i in new_str:
        new_word += i
    new_list.append(new_word)

print(new_list)