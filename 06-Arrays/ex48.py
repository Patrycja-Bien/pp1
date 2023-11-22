def create_2d_arr(x,y):
    # Initialize a 2D list with values of 0
    return [[0 for i in range(y)] for i in range(x)]

# Create a 3 by 5 two-dimensional list
my_2d_array = create_2d_arr(3, 5)

# Display the created list
for row in my_2d_array:
    print(row)

print(my_2d_array)
