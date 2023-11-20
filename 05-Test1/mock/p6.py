def f(number, even):
    sum = 0
    if even == True:
        while number > 0:
            if number % 2 == 0:
                sum += number%10
                number //= 10
            else:
                number //=10
    else:
        while number > 0:
            if number % 2 != 0:
                sum += number%10
                number //= 10
            else:
                number //=10
    return sum

if __name__ == "__main__":

    print(f(3124,True)) #returns 6
    print(f(3124,False)) #returns 4
    print(f(20576,False)) #returns 12
    print(f(20576,True)) #returns 8
    print(f(13115,True)) #returns 0

