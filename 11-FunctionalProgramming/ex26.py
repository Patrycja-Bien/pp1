"""
26.	Measuring stations recorded the following temperatures in degrees Celsius:
{"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
Write a program that creates a bar chart showing temperatures recorded in cities. 
Add a title for the chart and descriptions for the x and y axes. 
Tip: use the map() function to create two arrays of data for the chart.
"""
import matplotlib.pyplot as plt
import numpy as np

temps = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

x, y = map(list, zip(*temps.items()))

plt.title('Temperature Recorded in Cities')
plt.xlabel('Cities')
plt.ylabel('Temperature (°C)')

plt.bar(x,y, color = "pink")
plt.show()

