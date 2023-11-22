def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def display_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print() 

display_matrix(identity_matrix(3))
print()
display_matrix(identity_matrix(5))
print()
display_matrix(identity_matrix(8))