from random import random

list_numbers = []

len_list = 10
current_len = 0

while current_len <= len_list:
    list_numbers.append(random())
    current_len += 1

print(f"The largest number in the list containing 10 random numbers from 0 to 1 is: {str(max(list_numbers))}.")
