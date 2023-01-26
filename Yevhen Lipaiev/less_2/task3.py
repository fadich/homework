math = int(input('скільки буде 2+2*2'' Відповідь   '))
if math == 6:
    print(True)
    print("You are right")
elif math == 8:
    print(False)
    print("first plural")
elif -10000000 < math < 7:
    print(False)
    print("try one more")
elif math < 100000000:
    print(False)
    print("Try one more")


