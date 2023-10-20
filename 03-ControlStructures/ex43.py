sum = 0
i = 0
j = 1
li = [0, 1]
while i <= 2584:
    while j <= 4181:
        sum = i + j
        li.append(sum)
        i = j
        j = sum 
result = ' '.join(str(x) for x in li)
print(result)