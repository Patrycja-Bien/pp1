x = [2,3,2,5,8,1,9,8,8]
y = []

for i in x:
    y.append(i)

for j in y:
    if y.count(j) > 1:
        for i in range(y.count(j)):
            y.remove(j)
    else:
        continue

print("Array: "," ".join(str(i) for i in x))
print("Unique elements:"," ".join(str(j) for j in y))
