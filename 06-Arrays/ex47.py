x = [
    [7,3,7,9,0],
    [2,9,0,1,5],
    [3,8,6,4,7],
    [8,7,1,1,5]
    ]
sum = 0
for row in x:
    for element in row:
        if element == row[-1]:
            sum += element
        else:
            continue

print(sum)
