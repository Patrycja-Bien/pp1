def f(product_code):
    x = int(product_code[0])
    y = int(product_code[1])
    z = int(product_code[2])
    i = int(product_code[-1])
    sum = x + y + z
    remainder = sum%7
    if remainder == i:
        return True
    else:
        return False
print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))