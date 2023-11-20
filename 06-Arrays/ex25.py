x = [15, 8, 31, 47, 2, 19]

print(f"Array: {" ".join(str(i) for i in x)}")

sum = 0 
count = 0

while count < len(x):
    sum += x[count]
    count += 1

mean = sum/count

print(f"Mean: {mean}")