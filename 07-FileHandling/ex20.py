"""
20.	Using any text editor, create the following two text files:
MeatAndFish.txt
Skinless white meat
Tuna fish
Luncheon meat
Lean cuts of red meat

GrainsAndBread.txt
Bread
Rice
All purpose flour
Breakfast cereal
Pasta 
Then, write a program that creates the allproducts.txt file, 
in which save the contents of the MeatAndFish.txt and the GrainsAndBread.txt files.

"""
new = open("allproducts.txt", "w")
meat = open("MeatAndFish.txt", "r")
grains = open("GrainsAndBread.txt", "r")

for line in meat:
    new.write(line)
for line in grains:
    new.write(line)