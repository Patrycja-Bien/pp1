"""
27.	Write a program that computes the number of words in the following text. 
Use regular expressions.
To be, or not to be, that is the question
"""
x = "To be, or not to be, that is the question"
import re
words = re.split("\s",x)
count = len(words)
print("Number of words: ",count)
