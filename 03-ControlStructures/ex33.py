deci1 = deci = int(input("Enter decimal number: "))
bin =""
while deci > 0:
    rest = deci%2
    rest = str(rest)
    bin += rest
    deci = deci // 2
if len(bin) == 3:
    bin += "0"
elif len(bin) == 2:
    bin += "00"
elif len(bin) == 1:
    bin += "000"
elif len(bin) == 0:
    bin += "0000"
bin = bin[::-1]
print(f"{deci1}(10) = {bin}(2)")