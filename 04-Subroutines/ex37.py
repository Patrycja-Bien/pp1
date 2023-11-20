def f(n):
    sum = 0
    i = 0
    j = 1
    li = [0, 1]
    while len(li) <= n:
        sum = i + j
        li.append(sum)
        i = j
        j = sum 
    return li[n-1]
print(f(5))
print(f(9))
print(f(10))
print(f(1))
print(f(13))