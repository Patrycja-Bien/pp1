"""
15.	For the following text: I completely agree with you
write a program that calculates and displays the number of letters in each word. 
Use the map() and an anonymous functions to calculate the number of letters. 
Tip: to split text into words, use the split() function. Sample result:
Text: I completely agree with you
No. of letters in words: [1,10,5,4,3]
"""
text = "I completely agree with you"
print(f"Text: {text}")
textsplit = text.split()
n = list(map(lambda x: len(x),textsplit))
print(f"Np. of letters in words: {n}")