def f(number):
    number = (str(number))
    sum = 0
    if number.count("1") > 1:
        sum += number.count("1")
    if number.count("2") > 1:
        sum += 2*number.count("2")
    if number.count("3") > 1:
        sum += 3*number.count("3")
    if number.count("4") > 1:
        sum += 4*number.count("4")
    if number.count("5") > 1:
        sum += 5*number.count("5")
    if number.count("6") > 1:
        sum += 6*number.count("6")
    if number.count("7") > 1:
        sum += 7*number.count("7")
    if number.count("8") > 1:
        sum += 8*number.count("8")
    if number.count("9") > 1:
        sum += 9*number.count("9")
    return sum
print(f(1027))
print(f(230335))
print(f(513553007))

def g(number):
    sum = 0
    number = str(number)
    for i in range(1,10):
        i = str(i)
        if number.count(i) > 1:
            x = int(number.count(i))
            i = int(i)
            sum += i*x
    return sum

print(g(1027))
print(g(230335))
print(g(513553007))