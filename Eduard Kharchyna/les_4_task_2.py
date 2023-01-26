tel_number = input("Please input phone number in format ********** without + and where * is number+ ")
if tel_number.isdigit() and len(tel_number) == 10:
    print(f"Thanks.{tel_number} has valid phone number.")
else:
    print("You input number in wrong format.")
