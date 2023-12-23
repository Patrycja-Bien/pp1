"""
13.	In a beverage factory, a machine fills bottles of various capacities. A computer 
checks whether a bottle has been filled correctly. The allowable tolerance is 
2% for a 500ml bottle, 3% for a 1000ml bottle and 5% for a 1500ml bottle. 
Write a program that checks whether the bottle has been filled correctly or not. 
Define a higher order function. Sample result:
507: True
489: False
984: True
1032: False
1578: False
1430: True 
"""
def check(capacity, fill, tolerance):

    def tolerant():
        toler = capacity * tolerance / 100
        return abs(fill - capacity) <= toler

    return tolerant

check1 = check(500,507,2)
check2 = check(500,489,2)
check3 = check(1000,984,3)
check4 = check(1000,1032,3)
check5 = check(1500,1578,5)
check6 = check(1500,1430,5)

print(check1())
print(check2())
print(check3())
print(check4())
print(check5())
print(check6())
