def f(n):
    for i in n:
        if i == "0":
            continue
        elif i == "1":
            continue
        else:
            return False
    return True
    
x = input("Enter number: ")
print(f(x))