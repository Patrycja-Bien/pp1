"""
21.	Write a program containing a Statistics class that describes the properties of any set of 
numbers. The class should allow to:
a.	Add to the set of numbers, the next number read from the keyboard (store the numbers in the array)
b.	Display all numbers separated by a space
c.	Determine the greatest number
d.	Determine the smallest number
e.	Calculate the arithmetic mean of numbers
f.	Calculate of the median
g.	Display of calculated / determined statistical quantities (minimum, maximum, arithmetic mean, median)
Then, use the program for numbers:
12, 37, 6, 9, 17
"""
class Statistics():
    def __init__(self):
        self.nums = []
    def add(self,n):
        self.nums.append(n)
    def display_nums(self):
        print(" ".join(str(x) for x in self.nums)+"\n")
    def max(self):
        return max(self.nums)
    def min(self):
        return min(self.nums)
    def mean(self):
        return (sum(self.nums)/len(self.nums))
    def median(self):
        self.nums.sort()
        n = len(self.nums)
        mid = n // 2
        if n % 2 == 0:
            med = (self.nums[mid - 1] + self.nums[mid]) / 2
        else:
            med = self.nums[mid]
        return med
    def display(self):
        print("\nStatistics:")
        print("Max:", self.max())
        print("Min:", self.min())
        print("Mean:", self.mean())
        print("Median:", self.median())

stats = Statistics()
while True:
    try:
        num = float(input("Enter a number (or any non-numeric character to exit): "))
        stats.add(num)
    except ValueError:
        break  # Exit loop if a non-numeric character is entered
stats.display()