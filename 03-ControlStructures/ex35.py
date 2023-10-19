array = ""
for i in range(1,31):
    if i%3 == 0 and i%5 != 0:
        array += "THREE"
        array += " "
    elif i%3 != 0 and i%5 == 0:
        array += "FIVE"
        array += " "
    elif i%3 == 0 and i%5 == 0:
        array += "BINGO"
        array += " "
    else:
        i = str(i)
        array += i
        array += " "
print(array)