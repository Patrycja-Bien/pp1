x = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]

for i in range(len(x)):
    x[i][i] = 1

for row in x:
    print(" ".join(map(str, row)))