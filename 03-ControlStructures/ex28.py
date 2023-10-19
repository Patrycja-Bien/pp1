ean = input("Enter EAN-13 article number: ")
check_for_polish = ean[0:3]
check_for_polish = int(check_for_polish)
if len(ean) == 13:
    print("Article number is correct")
    if check_for_polish == 590:
        print("Article manufactured in Poland")
    else:
        print("Article NOT manufactured in Poland")
else:
    print("Article number is incorrect")