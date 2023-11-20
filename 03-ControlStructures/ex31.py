x = 5
y = 0
if x>0 and y>0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
elif x<0 and y>0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
elif x<0 and y<0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
elif x>0 and y<0:
    print(f"Point P({x},{y}) is in the forth quadrant of the coordinate system")
elif x==0 and y!=0:
    print(f"Point P({x},{y}) is on the OY axis of the coordinate system")
elif x==0 and y==0:
    print(f"Point P({x},{y}) is in the center of the coordinate system")
else:
    print(f"Point P({x},{y}) is on the OX axis of the coordinate system")
