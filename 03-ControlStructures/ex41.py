pin = "0805"
i = 3
while i != 0:
    guess = input("Enter the PIN code: ")
    if guess != pin:
        print("Incorrect...")
        i -= 1
    else:
        print("Correct")
        break
if i == 0:
    print("Sorry, your payment card has been blocked.")
