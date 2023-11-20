x = [8,2,5,1,9]
y = []

print(f"Array: {" ".join(str(i) for i in x)}")

for i in x:
    y.append(i**2)

print(f"Second power: {" ".join(str(i) for i in y)}")