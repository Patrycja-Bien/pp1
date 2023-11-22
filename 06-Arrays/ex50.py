x = [
    [-38, 19], 
    [5,40],
    [-7,11],
    [29,16]
    ]
min_value = float('inf')
max_value = float('-inf')

min_row, min_col = None, None
max_row, max_col = None, None

for i in range(len(x)):
    for j in range(len(x[0])):
        current_value = x[i][j]

        # Check for the smallest value
        if current_value < min_value:
            min_value = current_value
            min_row, min_col = i, j

        # Check for the largest value
        if current_value > max_value:
            max_value = current_value
            max_row, max_col = i, j

print("MAX: ",max_row,max_col)
print("MIN: ",min_row,min_col)