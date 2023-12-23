"""
11.	Write a program that calculates the average speed of a vehicle. Enter from 
the keyboard: a distance in km, a number of travel hours and a number of travel minutes. 
Use an anonymous function. Sample result:
Enter distance in km: 70
Enter number of travel hours: 1
Enter number of travel minutes: 23
Average speed: 50.6 km/h 
"""
d = int(input("Enter distance in km: "))
h = int(input("Enter number of travel hours: "))
m = int(input("Enter number of travel minutes: "))
avg_speed = lambda distance,hours,minutes: round(distance/(hours + minutes/60),1)
print(f"Average speed: {avg_speed(d,h,m)} km/h")