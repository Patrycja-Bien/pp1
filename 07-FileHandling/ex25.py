'''
25.	The announcement regarding the temperature forecast in 
degrees Celsius for the next three days was published on the Internet:
"Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
Create a program that calculates the average temperature. 
Use regular expressions to extract the values of temperatures from the message.

'''
import re
message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("(\d+)C",message)
sum = 0
count = 0
for i in temperatures:
    sum += int(i)
    count += 1
avr = sum/count
print("Sum: ",sum)
print("Number of numbers: ",count)
print("Average: ",avr)