def f(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        return number1 % number2
    else:
        return number1 ** number2

print(f(2,3, "+")) #returns 5
print(f(2,3, "%")) #returns 2
print(f(2,3, "**")) #returns 8
print(f(2,3, "*")) #returns 6
print(f(2,3, "-")) #returns -1
