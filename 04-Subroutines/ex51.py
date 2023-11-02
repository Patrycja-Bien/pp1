def sum(n):
    if n > 1:
        return n + sum(n-1)
    elif n == 1:
        return 1
    else:
        return "Not a natural number"
    
print(sum(10))
print(sum(3))
print(sum(1))
print(sum(0))