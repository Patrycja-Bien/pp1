"""
25.	Measuring stations recorded the following temperatures in degrees Celsius:
{"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
Write a program that displays the names of towns where positive temperatures were recorded. 
Use anonymous and filter() functions. Sample result:
Cities with positive temperatures: Krakow Sopot Opole
"""
temps = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
positive = list(filter(lambda temp: temps[temp] > 0, temps))
print(f"Cities with positive temperatures: {" ".join(x for x in positive)}")