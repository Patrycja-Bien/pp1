a = (input("Input a: "))
a = float(a)
b = input("Input b: ")
b = float(b)
c = input("Input c: ")
c = float(c)
tri_circ = a + b + c
float(tri_circ)
half_tri_circ = tri_circ / 2
tri_area = (half_tri_circ*(half_tri_circ - a)*(half_tri_circ - b)*(half_tri_circ - c))**(1/2)
print(f"Triangle area: {tri_area}")
print(f"Triangle circumference: {tri_circ}")