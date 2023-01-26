import random
computer_number = random.randint(1, 10)
user_number = input("Guess what integer number from 1 to 10 was generated:")
if computer_number == int(user_number):
    print("Congratulation! You are right.")
else:
    print(f"You are wrong. The right answer is {computer_number}.")