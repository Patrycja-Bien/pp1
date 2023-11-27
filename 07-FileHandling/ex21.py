#21.	Create a program that writes to 
#a text file integer numbers in the range <1,50>, 
#every number in a separate line.

x = open("nums.txt", "w")
for i in range(1,51):
    x.write(str(i)+"\n")