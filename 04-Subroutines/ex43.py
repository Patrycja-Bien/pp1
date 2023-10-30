def f(name):
    result = ""
    words = name.split(" ")
    for i in words:
        y = i[0]
        result += y
    return result

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))


