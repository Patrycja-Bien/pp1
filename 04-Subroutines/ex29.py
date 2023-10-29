def f(amount_to_pay):
    if amount_to_pay == 5:
        return 1
    elif amount_to_pay == 2:
        return 1
    else:
        three = amount_to_pay//5
        two = amount_to_pay%5
        two = two//2
        one = two%2
        return three + two + one
print(f(23))
print(f(8))
print(f(2))
print(f(0))