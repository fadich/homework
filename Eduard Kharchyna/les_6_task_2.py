from random import randint

list_1 = []
list_2 = []

while len(list_1) < 10 and len(list_2) < 10:
    list_1.append(randint(1, 10))
    list_2.append(randint(1, 10))

unique_list = list(set(list_1 + list_2))
