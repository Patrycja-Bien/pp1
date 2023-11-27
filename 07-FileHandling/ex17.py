#Find any text file on the Internet that contains at least 30 lines of text and download that file to your computer. 
#Then, write a program that displays the first five lines from the file and then waits for the Enter key to be pressed. 
#The program repeats displaying the next five lines from the file, waiting for the Enter key to be pressed each time.

f = open("lovecraft.txt", 'r')
check = True
for i in range(5):
    print(f.readline())
while check == True:
    x = input("Press Enter to show 5 more lines: ")
    print()
    if x == "":
        for i in range(5):
            print(f.readline())
    else:
        check = False
    
