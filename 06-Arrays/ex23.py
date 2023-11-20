x = [-15, 8, -31, 47, -2, 19]

max = 0
for i in x:
    if i > max:
        max = i
    else:
        continue

min = 0
for i in x:
    if i < min:
        min = i
    else:
        continue

print(f"Max: {max}")

print(f"Min: {min}")