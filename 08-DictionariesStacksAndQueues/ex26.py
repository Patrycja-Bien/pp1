"""
26.	Following the example of stack.py, create a queue.py module in which define queue handling. 
Then write a program that imports the queue.py module. 
Add and remove values from the queue. Display its content.
"""
import queue

queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
print(queue.display())
queue.pop()
print(queue.display())