"""
21.	An array contains numbers from 1 to 20. Write a program that displays only numbers 
divisible by 2 and 3 without remainder. Use the filter() and an anonymous function.
"""
numbers = [i for i in range(1,21)]
print(f"Numbers: {" ".join(str(n) for n in numbers)}")
divs = list(filter(lambda n: n%2 == 0 and n%3 == 0, numbers))
print(f"Numbers divisible by 2 and 3 without remainder: {" ".join(str(n) for n in divs)}")