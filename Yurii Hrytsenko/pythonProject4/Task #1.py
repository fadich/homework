from random import randint

flag = True

while flag:
    number = randint(0, 9)
    print("I guessed a number from 0 to 9, try to guess!")
    print("Or enter 'quit' to exit.")
    try_count = 0

    while try_count < 6:
        variant = input("").lower().strip()

        if variant == "quit":
            flag = False
            break

        if variant.isdigit():
            variant = int(variant)
            if not (-1 < variant < 10):
                print("Enter only numbers from 0 to 9!")
        else:
            print("Enter only numbers from 0 to 9!")
            continue

        if variant == number:
            print("Okay this time you win!\n")
            break
        elif variant > number:
            print(f"NO, my variant is smaller! {5 - try_count} tries left.")
            try_count += 1
        elif variant < number:
            print(f"NO, my variant is bigger! {5 - try_count} tries left.")
            try_count += 1
        else:
            print(f'Your variant is out of range! {5 - try_count} tries left.')
            try_count += 1

        if try_count == 6:
            print("Sorry you lose. Try again!\n")

    try_count = 0
