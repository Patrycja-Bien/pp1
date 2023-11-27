"""
29.	The grades.txt file contains student’s grades. 
Create the file in any text editor with the content as below:
Name: Peter
Grades: 3.5, 4.0, 5.0, 4.5, 3.5, 3.0, 5.0
Then, create a program that calculates the arithmetic mean of student’s grades.
"""
import re
file = open("grades.txt", "r")
x = file.read()
grades = re.findall(r'\b\d+\.\d+\b',x)
print(grades)
sum = 0
num = len(grades)
for i in grades:
    sum += float(i)
mean = sum/num
print(mean)