x = int(input("Enter number: "))
arr = [10,2,3,4,5,6.5,7,8]
count = 0

for i in arr:
    if x < i:
        count += 1
    else:
        continue

print(count)