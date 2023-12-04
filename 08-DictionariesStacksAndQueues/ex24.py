"""
24.	Write a program that converts any natural number to a binary number. Use the stack. To convert a number, divide the number by 2, 
each time taking the remainder of the division and putting the remainder on the stack. 
Repeat the division until the number you are dividing is zero. Then pop and display all values from the stack. Sample result for number 18:
Division	Remainder
18 / 2 = 9	0
9 / 2 = 4	1
4 / 2 = 2	0
2 / 2 = 1	0
1  / 2 = 0	1
Natural number: 18
Binary number: 10010 

"""
final = ""
import stack
num = int(input("Enter natural number: "))
while num != 0:
    stack.push(num % 2)
    num //= 2
if num < 0:
    print("That's not a natural number...")
while not stack.empty():
    final += str(stack.pop())
print(f"Binary number: {final}")
