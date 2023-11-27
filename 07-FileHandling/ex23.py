'''
23.	Create a program that saves to a text file integer 
numbers in the range <1,10> with their second and third power. Sample result:
1,1,1
2,4,8
3,9,27
4,16,64
…
'''
file = open("power.txt", "w")
for i in range(1,11):
    file.write(str(i)+","+str(i**2)+","+str(i**3)+"\n")