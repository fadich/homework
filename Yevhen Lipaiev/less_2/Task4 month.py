month = int(input('Напиши числом місяць в якому ти народився'  ))

if month <= 0 or month >= 13:
    print("error")
elif month <= 2 or month == 12:
    print("Winter")
elif month <= 5:
    print("Spring")
elif month <= 8:
    print("Summer")
elif month <= 11:
    print("Fall")
