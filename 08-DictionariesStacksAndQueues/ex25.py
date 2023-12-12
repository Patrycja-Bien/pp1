"""
25.	Search the Internet and familiarise yourself with RPN (Reverse Polish Notation). Then, write a program that calculates RPN expressions. 
RPN can be conveniently evaluated using a stack structure. A user can enter from the keyboard any number, an operator (+ - * / ) or the equal sign (=).
a.	If the entered value is a number, push the number on to the stack
b.	If the entered value is an operator, pop two items from the top of the stack, do the calculation, and push the result of the operation on to the stack.
c.	If the entered value is an equal sigh, pop the final result from the stack and display the result of calculation.
Using the program, calculate the value of RPN expressions:
Expression	RPN (Reverse Polish Notation)
2 + 3 =	                        2 3 + =
2 * (4 + 1)	                    2 4 1 + * =
(2 + 3) * ( 4 + 5) =	        2 3 + 4 5 + * =
8 / (3 + 1) * (3 - 2 + 4) = 	8 3 1 + / 3 2 – 4 + * =
"""
import stack
check = True
nums = ["0","1","2","3","4","5","6","7","8","9"]
opps = ["+","-","*","/"]
result = ""
calculation = ""
while check:
    digit = input("Enter expression: ")
    calculation += digit
    if digit in nums:
        stack.push(int(digit))
    elif digit in opps:
        result += str(stack.pop())
        result += str(stack.pop())
        result += digit
    elif digit == "=":
        check = False
        calculation = calculation[:-1]
        print("Calculation: ",eval(calculation))
        print("Result: ", result)
