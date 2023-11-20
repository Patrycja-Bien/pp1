def power(x,n):
    if n != 1:
        return x * x**(n-1)
    else:
        return x

print(power(5,3))
print(power(5,2))
print(power(2,10))
print(power(2,-3))
print(power(2,-1))
print(power(10,0))