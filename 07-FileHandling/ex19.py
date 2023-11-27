#19.	Find any text file on the Internet and download it to your computer. 
#Then, write a program that copies the contents of this file to the copylines.txt file. 
#Copy the contents of the file line by line. 

t = open("lovecraft.txt", "r")
new = open("copy19.txt", "w")
for line in t:
    new.write(line)
