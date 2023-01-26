limit_n = int(input("Please input number N (upper limit): "))
number_a = int(input("Please input number A: "))
number_b = int(input("Please input number B: "))
start_number = 1
while start_number < limit_n:
    if start_number % number_a == 0 and start_number % number_b == 0:
        print(f"Bingo {start_number} is a multiple of A and B.")
        break
    elif start_number % number_a == 0:
        print(start_number, "is a multiple of A.")
    elif start_number % number_b == 0:
        print(start_number, "is a multiple of B.")
    start_number +=1