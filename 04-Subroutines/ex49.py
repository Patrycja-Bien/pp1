def f(dice):
    one = dice.count("1")
    two = dice.count("2")
    three = dice.count("3")
    four = dice.count("4")
    five = dice.count("5")
    six = dice.count("6")
    x = max(one, two, three, four, five, six)
    if x == one:
        return "1"
    elif x == two:
        return "2"
    elif x == three:
        return "3"
    elif x == four:
        return "4"
    elif x == five:
        return "5"
    else:
        return "6"

print(f("5233165554211"))
print(f("2133"))