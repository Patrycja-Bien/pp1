def f(detector):
    x = 0
    y = 0
    for i in detector:
        if x == 3:
            y += 1
        if i == "+":
            x += 1
        else:
            x -= 1
    if y != 0:
        return True
    else:
        return False
    
print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))