"""
10.	Write a program that calculates the average speed of a vehicle. Enter from the 
keyboard: a distance in km, a number of travel hours and a number of travel minutes. 
Define a function avg_speed(distance,hours,minutes) that returns the calculated average 
speed. Sample result:
Enter distance in km: 70
Enter number of travel hours: 1
Enter number of travel minutes: 23
Average speed: 50.6 km/h 
"""
d = int(input("Enter distance in km: "))
h = int(input("Enter number of travel hours: "))
m = int(input("Enter number of travel minutes: "))
def avg_speed(distance,hours,minutes):
    t = hours + minutes/60
    return f"Average speed: {round(distance/t,1)} km/h"

print(avg_speed(d,h,m))