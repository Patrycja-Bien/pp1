"""
29.	At one of the Olympic Games, the medal classification is as follows:
{"country":"Denmark","gold":2,"silver":4,"bronze":6}
{"country":"Finland","gold":5,"silver":0,"bronze":4}
{"country":"USA","gold":12,"silver":5,"bronze":11}
{"country":"Peru","gold":0,"silver":1,"bronze":7}
Write a program that creates a bar chart showing the total number of medals won by each 
country. Add a title for the chart and descriptions for the x and y axes. 
Tip: Use the map() function to create arrays of data for your chart.
"""
import matplotlib.pyplot as plt

games = [
{"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}]

country = list(map(lambda n: n["country"], games))
gold = list(map(lambda x: x["gold"], games))
silver = list(map(lambda x: x["silver"], games))
bronze = list(map(lambda x: x["bronze"], games))
medals = list(map(lambda g,s,b: g+s+b, gold, silver,bronze))

plt.title("Olympic Medals")
plt.xlabel("Countries")
plt.ylabel("Number of medals won")
plt.bar(country, medals, color = "pink")
plt.show()
