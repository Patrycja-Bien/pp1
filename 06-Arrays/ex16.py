x = [
    [3,9,2],
    [2,4,5],
    [7,1,6],
    [0,4,8]
    ]
sum_odd = 0
for row in x:
    for element in row:
        if element%2 == 0:
            sum_odd += element 
print(sum_odd)
