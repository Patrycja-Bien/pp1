number = input("Enter phone number: ")
splice = number[:3] + "-" + number[3:6] + "-" + number[6:]
print(f"Phone number: {splice}")