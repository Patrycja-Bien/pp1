a = 4
b = 15
side1 = "*"
side2 = a - 2
hole = " "*(b - 2)
print(side1*b)
while side2 > 0:
    print("*" + hole + "*")
    side2 = side2 - 1
print(side1*b)
