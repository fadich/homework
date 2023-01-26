list_100 = list(range(1, 100))
list_7_not_5 = []

index = 0
while index < len(list_100):
    if list_100[index] % 7 == 0 and list_100[index] % 5 != 0:
        list_7_not_5.append(list_100[index])
    index += 1

print(list_7_not_5)

'''Рішення за допомогою for'''
for_list = [x for x in range(1, 100) if x % 7 == 0 and x % 5 != 0]
print(for_list)
