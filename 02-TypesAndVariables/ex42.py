x = input("Enter four-digit binary number: ")
if len(x) != 4:
    print("Wrong digit number")

zero = x[0]
zero = int(zero)

one = x[1]
one = int(one)

two = x[2]
two = int(two)

three = x[3]
three = int(three)

decimal = 0

if zero == 1:
    decimal += 8
if one == 1:
    decimal += 4
if two == 1:
    decimal += 2
if three == 1:
    decimal += 1
print(f"Binary number in decimal notation: {decimal}")