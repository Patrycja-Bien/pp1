"""
24.	An object contains a list of coordinates of points on the plane, as a two-dimensional array. 
Define a C class that allows you to create an object. Provide the list of coordinates of points at 
the time of creating the object. In the class C, define a method m(n) that returns true when at least 
n points are in the first quadrant of the coordinate system (both point coordinates are greater 
than 0), or false otherwise. Sample result:
C([[2,3],[1,8],[-6,4],[3,-7]])
m(2) returns True
m(3) returns False
"""
class C():
    def __init__(self,coords):
        self.coords = coords
    def m(self,n):
        result = [point for point in self.coords if point[0] > 0 and point[1] > 0]
        return len(result) >= n

c = C([[2,3],[1,8],[-6,4],[3,-7]])
print(c.m(2)) #returns True
print(c.m(3)) #returns False