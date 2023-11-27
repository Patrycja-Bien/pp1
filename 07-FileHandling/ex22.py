#22.	Create a program that writes 50 random integers between 100 and 999 
#to a text file, each number on a separate line.

import random
x = open("random.txt", "w")
y = [random.randint(100,999) for i in range(50)]
for i in y:
    x.write(str(i)+"\n")