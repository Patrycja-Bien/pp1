x = [15, 8, 31, 47, 2, 19]

print(f"Array: {" ".join(str(i) for i in x)}")

sum = 0
for i in x:
    sum += i

mean = sum/len(x)

print(f"Mean: {mean}")