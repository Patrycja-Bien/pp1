"""
17.	Write a program that spells any text entered from the keyboard, 
using ICAO spelling alphabet:
https://en.wikipedia.org/wiki/NATO_phonetic_alphabet
Create a dictionary in which you put all the letters and the corresponding words. 
Then, try to spell your name and three other words. Sample result:
Enter text: uek
Spelled text: Uniform Echo Kilo
"""
icao = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliet',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'X-ray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}

word = input("Enter word: ")
result = []
word = word.upper()
for letter in word:
    result.append(icao[letter])
print(f"Word: {word}")
print(f"ICAO: {" ".join(str(i) for i in result)}")