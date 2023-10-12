credit = input("Enter card number: ")
split = credit[:4] + " " + credit[4:8] + " " + credit[8:12] + " " + credit[12:]
print(f"Card number: {split}")