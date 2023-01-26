# homework LMS
# ex1
import random
print('The Greatest Number')
list_of_randoms = []
i = 0
while i <= 10:
    list_of_randoms.append(random.randint(0,100))
    i += 1
print(f'The generated list is {list_of_randoms}\n'
      f'The biggest number in this list is {max(list_of_randoms)}')

# ex2
print('\nExclusive common numbers\n')
list_a = []
list_b = []
i = 0
while i <= 10:
    list_a.append(random.randint(0,10))
    list_b.append(random.randint(0,10))
    i += 1

common_wo_duplicates = set(list_a) & set(list_b)
print(f'The lists are {list_a} and {list_b}\n'
      f'The common integers are: {list(common_wo_duplicates)}')

# ex3
'''Я знаю, в умові написано для ітерації while, але ж for-in набагато
набагато набагато зручніше :('''

print('\nExtracting numbers\n')
master_list = range(100)
selected_list = []
for element in master_list:
    if element % 7 == 0 and element % 5 != 0:
        selected_list.append(element)
print(selected_list)