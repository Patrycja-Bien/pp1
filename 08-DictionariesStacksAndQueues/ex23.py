"""
23.	Write a program, in which, import the module stack.py. Then, do the following:
a.	Display stack
b.	Put the number 2 on the stack
c.	Put the number 14 on the stack
d.	Put the number 9 on the stack
e.	Display stack
f.	Get element from stack
g.	Display stack
h.	Put the number 31 on the stack
i.	Put the number 6 on the stack
j.	Display stack
k.	Get two elements from stack
l.	Display stack

"""
import stack
print("a.	Display stack")
stack.display()
print("b.	Put the number 2 on the stack")
stack.push(2)
print("c.	Put the number 14 on the stack")
stack.push(14)
print("d.	Put the number 9 on the stack")
stack.push(9)
print("e.	Display stack")
stack.display()
print("f.	Get element from stack")
stack.pop()
print("g.	Display stack")
stack.display()
print("h.	Put the number 31 on the stack")
stack.push(31)
print("i.	Put the number 6 on the stack")
stack.push(6)
print("j.	Display stack")
stack.display()
print("k.	Get two elements from stack")
stack.pop()
stack.pop()
print("l.	Display stack")
stack.display()