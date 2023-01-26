import random
# Task 1

lst = random.sample(range(1, 1001), 10)
print('The largest number is >> ',max(lst))
# another way
count = 0
numbers = []

while count < 10:
    numbers.append(random.randint(1,1000))
    count+=1

print('Another largest number is ',max(numbers))

# Task 2
first_lst = random.sample(range(1, 1001), 10)
second_lst = random.sample(range(1, 1001), 10)

first_lst.extend(second_lst)
common =set(first_lst)

print('Here are only unique numbers ',common)

# Task 3

n = 0
numbers_100 = []

while n<100:
    n+=1
    numbers_100.append(n)

index = -1
length = 100
multiples_7 = []

while length>0:
    length-=1
    index+=1
    if numbers_100[index] % 7 == 0 and numbers_100[index] % 5 !=0:
        multiples_7.append(numbers_100[index])

print('Multiples of 7 ',multiples_7)