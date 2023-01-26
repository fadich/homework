
while True:
    N = input("Enter N:\n")
    A = input("Enter A:\n")
    B = input("Enter B:\n")

    if N == "quit" or A == "quit" or B == "quit":
        break

    if not N.isdigit() or not A.isdigit() or not B.isdigit():
        print("Use numbers only!")
        continue

    N, A, B = int(N), int(A), int(B)

    number = 1

    while number != N:
        if number % A == 0 and number % B == 0:
            print(f"Бінго! Число {number} ділеться як на A, так і на B!")
            break
        elif number % A == 0:
            print(f"Число {number} кратне A")
        elif number % B == 0:
            print(f"Число {number} кратне B")

        number += 1
