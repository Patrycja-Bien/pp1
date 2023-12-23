"""
20.	An array contains numbers from 1 to 20. Write a program that calculates and displays 
their third power. Use the map() and an anonymous function.
"""
numbers = [i for i in range(1,21)]
print(f"Numbers: {" ".join(str(n) for n in numbers)}")
power = map(lambda n: n**3, numbers)
print(f"Third power: {" ".join(str(n) for n in power)}")