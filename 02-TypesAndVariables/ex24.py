registr = input("Enter vehicle number: ")
x = "KR"
y = "KK"
z = registr.startswith("KR")
a = registr.startswith("KK")
check = bool(a or z)
print(f"Car from Kraków: {check}")