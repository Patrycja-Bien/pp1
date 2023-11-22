x = [
    [1,2,3,4],
    [5,6,7,8]
    ]

for row in x:
    print(" ".join(str(i) for i in row), end = " ")
    print()