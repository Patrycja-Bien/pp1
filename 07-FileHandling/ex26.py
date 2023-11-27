"""
26.	Write a program that calculates the number of vowels in the text:
To be, or not to be, that is the question
Use regular expressions and the findall() method.
"""
x = "To be, or not to be, that is the question"
import re
vowels = re.findall("[aeiou]",x)
count = len(vowels)
print("Number of vowels: ",count)