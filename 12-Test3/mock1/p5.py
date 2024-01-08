"""
(p5.py) A counter allows you to count any elements. 
Define a class C to create counters. The initial value 
of the counter is assigned when the object is created. 
The class contains the following methods:
•	m1() - returns the counter value
•	m2() - increases the counter value by 1
•	m3() - decreases the counter value by 1
•	m4(n) - increases/decreases the counter value by n
•	__str__ - returns a string representation of the 
counter value
Example:
c=C(5)
c.m1()  5
c.m2()
c.m1()  6
c.m4(-8)
c.m1()  -2
c.m3()
c.m1()  -3
c.m4(10)
c.m1()  7
c.__str__()  "7"
"""
class C():
    def __init__(self,count):
        self.count = count
    def m1(self):
        return self.count
    def m2(self):
        self.count += 1
    def m3(self):
        self.count -= 1
    def m4(self,n):
        self.count += n
    def __str__(self):
        return str(self.count)
if __name__ == "__main__":
    c=C(5)
    print(c.m1())
    c.m2()
    print(c.m1())
    c.m4(-8)
    print(c.m1())
    c.m3()
    print(c.m1())
    c.m4(10)
    print(c.m1())
    print(c.__str__())