i = 0
sum = 0
y = 1
while y != 0:
    x = int(input("Enter number: "))
    if x == 0:
        break
    i += 1
    sum += x
   
print(f"RESULT: Quantity={i}, Sum={sum}, Mean={round(sum/i)}")