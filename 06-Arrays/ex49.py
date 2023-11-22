x = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ]

# Populate the list with multiplication table values
for i in range(1, len(x) + 1):
    for j in range(1, len(x[0]) + 1):
        x[i-1][j-1] = i * j

# Display the modified array (multiplication table)
for row in x:
    print(" ".join(str(i) for i in row))
