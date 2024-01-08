"""
(p7.py) A computer system registers all entries into the car park ("in") and exits 
from the car park ("out"). Define a function f(d) that for the registered data d 
returns an array containing the registration numbers of vehicles that remain in the 
car park, in alphabetical order. Example:
cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],
["BA123","out"],["KR234","in"]]
f(cars) -> ["BA111","GX444","KR234"]
cars1 = [["KR234","in"],["KR234","out"]]
f(cars1) -> []
"""
def f(d):
    result = []
    for i in d:
        if i[1] == "in":
            result.append(i[0])
        elif i[1] == "out" and i[0] in result:
            result.remove(i[0])
        else:
            continue
    result.sort()
    return result

if __name__ == "__main__":
    cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],
    ["BA123","out"],["KR234","in"]]
    print(f(cars))
    cars1 = [["KR234","in"],["KR234","out"]]
    print(f(cars1))