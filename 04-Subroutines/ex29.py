def f(amount_to_pay):
    three = amount_to_pay//5
    if amount_to_pay%5 == 0:
        return three
    else:
        two = amount_to_pay%5
        if two%2 == 0:
            return three + two//2
        else:
            two = two//2
            one = two%2
            return three + two + one
print(f(23))
print(f(8))
print(f(2))
print(f(0))