def f(n):
    x = ""
    for i in range(n):
        if i != n - 1:
            x += "*/"
        else:
            x += "*"
    return x

print((f(4)))
print(f(1))

