def f(array2D):
    n = len(array2D)

    # Calculate the sums of rows and columns
    row_sums = [sum(row) for row in array2D]
    col_sums = [sum(array2D[row][col] for row in range(n)) for col in range(n)]

    # Check if sums are equal for each row and its corresponding column
    for i in range(n):
        if row_sums[i] != col_sums[i]:
            return False
    return True

if __name__ == "__main__":
    print(f([[3,7,2],[4,2,5],[5,2,1]]))
    print(f([[3,7,2],[4,2,5],[9,2,1]]))
