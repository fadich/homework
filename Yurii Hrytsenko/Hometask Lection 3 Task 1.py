# Task 1

str_ = input("Enter your string: \n")
result = ""

if len(str_) < 2:
    result = ""
else:
    result = str_[:2] + str_[-2:]

print(result)