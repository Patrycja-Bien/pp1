"""
8.	Write a program that converts speed in meters per second to speed in kilometers per 
hour. Define a function ms_to_kmh(ms) that returns the calculated speed in km/h. 
Sample result:
10 m/s = 36 km/h
35 m/s = 126 km/h
"""
def ms_to_kmh(ms):
    return ms*3.6
n1 = 10
n2 = 35
print(f"{n1} m/s = {ms_to_kmh(n1)} km/h")
print(f"{n2} m/s = {ms_to_kmh(n2)} km/h")