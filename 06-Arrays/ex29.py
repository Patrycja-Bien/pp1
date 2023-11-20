x = [4,36,12,28,9,44,5]
y = [5,1,36]

z = []

for i in x:
    if i != y[0] and i != y[1] and i != y[2]:
        z.append(i)

print(" ".join(str(i) for i in z))