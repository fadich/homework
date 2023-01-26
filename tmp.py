from collections import defaultdict
from pprint import pprint

RES = "1112132321 1112232121 2113111122 3313132133 1121312322 1223231323 3121331221 3211333313 1123331321 3333323321"
TABLE = {
    0: [3, 1, 1, 3, 1, 1, 3, 1, 3, 1],
    1: [3, 1, 3, 3, 1, 3, 3, 3, 1, 1],
    2: [1, 3, 3, 3, 1, 1, 3, 1, 3, 1],
    3: [1, 1, 1, 3, 3, 1, 3, 3, 1, 3],
    4: [3, 1, 3, 3, 1, 3, 1, 1, 1, 1],
    5: [1, 1, 3, 1, 3, 1, 3, 3, 1, 1],
    6: [3, 1, 1, 3, 1, 1, 3, 3, 1, 3],
    7: [3, 1, 1, 1, 3, 3, 3, 1, 3, 1],
    8: [2, 2, 2, 3, 3, 3, 2, 3, 2, 1],
    9: [3, 3, 1, 3, 1, 1, 3, 1, 1, 3],
}

results = map(int, RES.replace(" ", ""))

marks = defaultdict(int)
for i, result in enumerate(results):
    index = i % 10
    number = i // 10
    if index == 8:
        print(result, TABLE[index][number])
        marks[index] += 2 if result == TABLE[index][number] else 0
    else:
        if result == TABLE[index][number]:
            marks[index] += 2
        elif result == 2:
            marks[index] += 1
        else:
            marks[index] += 0

pprint(marks)

"""
L   10
P   11


Do  2
D   6
A   8
Z   11
V   12
M   14
N   15

"""
