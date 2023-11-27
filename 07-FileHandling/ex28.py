"""
28.	Find any text file on the Internet and download it to your computer. 
Then, write a program that displays all words with at least six letters from the file. 
Display each word on a separate line. Use regular expressions.
"""
import re
file = open("lovecraft.txt", "r")
x = file.read()

# Function to extract words with at least six letters from a given text
def extract_words(text):
    return re.findall(r'\b\w{6,}\b', text)

# Extract and display words with at least six letters
selected_words = extract_words(x)
print("Words with at least six letters:")
for word in selected_words:
    print(word)