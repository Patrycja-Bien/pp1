"""
30.	In a beverage factory, a machine fills 500ml bottles. The computer checks whether 
the bottle has been filled correctly. For a 500ml bottle, the allowable tolerance is 2%. 
In the last ten bottles checked, the filling was:
508,500,512,499,492,511,503,476,501,509
Write a program that calculates the percentage of incorrectly filled bottles. 
Use the filter() along with a higher order function. Sample result:
Bottle capacity:    500ml
Filling tolerance:  2%
Filled bottles:     508,500,512,499,492,511,503,476,501,509
Incorrectly filled: 30%
"""
capacity = 500
tolerance = 2

bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

def is_incorrectly_filled(fill):
    x = capacity * tolerance / 100
    return abs(fill - capacity) > x

result = list(filter(is_incorrectly_filled, bottles))

incorrect = (len(result) / len(bottles)) * 100

print("Bottle capacity:", capacity,"ml")
print("Filling tolerance:", tolerance,"%")
print("Filled bottles:", " ".join(str(b) for b in bottles))
print("Incorrectly filled:", f"{incorrect}%")
