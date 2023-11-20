x = [34,7,19,4,21,8]

even = 0
while even == 0:
    for i in x:
        if i%2 == 0:
            even += 1
        else:
            continue

print(even)
