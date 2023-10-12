import math
circu = input("Enter tree circumference: ")
circu = float(circu)
diam = circu / math.pi
check = diam >= 50
print(f"Tree can be cut down: {check}")