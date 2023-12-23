"""
7.	Write a program that calculates the arithmetic mean of two numbers. 
Use an anonymous function. Sample result:
"""
n1 = 5
n2 = 10
mean = lambda x,y: (x+y)/2
result = mean(n1,n2)
print(f"Arithmetic mean of {n1} and {n2} is {result}")