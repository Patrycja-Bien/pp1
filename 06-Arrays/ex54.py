def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def transpose_matrix(m):
    return [[row[i] for row in m] for i in range(len(m[0]))]


print(identity_matrix(5))
print()
print(transpose_matrix(5))