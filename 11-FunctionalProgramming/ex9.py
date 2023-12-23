"""
9.	Write a program that converts speed in meters per second to speed in kilometers 
per hour. Use an anonymous function. Sample result:
"""
n1 = 10
n2 = 35
ms_to_kmh = lambda x: x*3.6
print(f"{n1} m/s = {ms_to_kmh(n1)} km/h")
print(f"{n2} m/s = {ms_to_kmh(n2)} km/h")