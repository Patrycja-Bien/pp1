def f(n1,n2,n3):
    i = 0
    if n1 < 0:
        i += 1
    if n2 < 0:
        i += 1
    if n3 < 0:
        i += 1
    if i != 0:
        return True
    else:
        return False

print(f(11,6,-4))
print(f(5,4,14)) 