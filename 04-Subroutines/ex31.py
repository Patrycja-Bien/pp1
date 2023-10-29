def f(x,y):
    sum = 0
    for i in range(x,y+1):
        if i < 0:
            if i%2 == 0:
                 sum += 1
            else:
                continue
        else:
            break
    return sum
print(f(-7,8))
print(f(-1,11)) 
