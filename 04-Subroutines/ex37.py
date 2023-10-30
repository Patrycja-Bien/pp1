def f(n):
    sum = 0
    i = 0
    j = 1
    li = [0, 1]
    while i <= 10000:
        while j <= 20000:
            sum = i + j
            li.append(sum)
            i = j
            j = sum 
    return li[n-1]
print(f(5))
print(f(9))