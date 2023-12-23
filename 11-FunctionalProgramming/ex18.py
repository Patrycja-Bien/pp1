"""
18.	A speed camera located in a city measures the speed of passing vehicles. The maximum 
permitted speed of vehicles is 50 km/h. In the last minute, the speed camera recorded the 
following values: 48,47,54,50,42,68,39,46
Write a program that displays speed values higher than the allowed speed. 
Use anonymous and filter() functions. Sample result:
Recorded values: 48,47,54,50,42,68,39,46
Speed too high: 54,68
"""
speeds = [48,47,54,50,42,68,39,46]
print(f"Recorded speeds: {",".join(str(x) for x in speeds)}")
ticket = list(filter(lambda speed: speed>50,speeds))
print(f"Speed too high: {",".join(str(x) for x in ticket)}")
