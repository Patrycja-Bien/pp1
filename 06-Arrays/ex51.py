x = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

for row in x:
    print(" ".join(str(i) for i in row))

print()

newx = [
    x[2],
    x[1],
    x[0]
]

for row in newx:
    print(" ".join(str(i) for i in row))

print()