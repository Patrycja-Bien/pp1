def f(number, even):
    if even == True:
        sum = 0
        while number > 0:
            if number %2 == 0:
                sum += number % 10
                number //= 10
            else:
                number //= 10
        return sum
    else:
        sum = 0
        while number > 0:
            if number %2 != 0:
                sum += number % 10
                number //= 10
            else:
                number //= 10
        return sum

print(f(3124,True))
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))
print(f(13115,True))
