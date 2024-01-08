"""
(p1.py) Create a function f(n) that returns the difference between the largest and 
smallest odd digit contained in the number n. When the number n does not contain odd 
digits, the function returns -1. Example:
f(10852) -> 4
f(7235973) -> 6
f(4388) -> 0
f(846206) -> -1
"""
def f(n):
    result = []
    for digit in str(n):
        if int(digit)%2 != 0:
            result.append(digit)
    if len(result) == 0:
        return -1
    else:
        return int(max(result)) - int(min(result))
if __name__ == "__main__":    
    print(f(10852))
    print(f(7235973))
    print(f(4388))
    print(f(846206))