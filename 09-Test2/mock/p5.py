"""
(p5.py) Create a function f(first_letter,last_letter) that, for the data.txt file, returns the 
number of words that start with the first_letter and end with the last_letter. 
"""
import re
def f(first_letter,last_letter):
    with open("data.txt","r",encoding="UTF-8") as file:
        data = file.read()
        pattern = rf'\b{re.escape(first_letter)}[a-zA-Z]*{re.escape(last_letter)}\b'
        matches = re.findall(pattern, data)
        return len(matches)
    
if __name__ == "__main__":
    print(f("w","d"))