arr = [1,2,3,4,5,6,7,8,9,10]
new = []

for i in arr:
    if i%2 == 0:
        new.append(i)
for i in arr:
    if i%2 != 0:
        new.append(i)
arr = new
print(arr)