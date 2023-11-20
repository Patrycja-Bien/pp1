x = [
    [True,False],
    [True,True],
    [False,False]
    ]

print("Before:", x)

for i in range(len(x)):
    for j in range(len(x[i])):
        x[i][j] = not x[i][j]

print("After: ", x)