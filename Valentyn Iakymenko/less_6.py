import random
  # Task1
lists= random.sample(range(0, 100), 10)
print(lists)
print(max(lists))
  # Task2
a= random.sample(range(1, 11), 10)
b= random.sample(range(1, 11), 10)
c= list(set(a + b))
print(c)
  # Task3

lists= random.sample(range(1,101), 100)
print(lists)
result = []
for number in lists:
    if number % 7 == 0 and number % 5 !=  0:
        print(number)
        result.append(number)
        print(result)

