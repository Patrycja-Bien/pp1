"""
11.	Create a dictionary that describes your favorite book or 
movie with at least five key-value pairs. 
Then, create a program that writes the dictionary data 
to the favourite.json file. Use the dump() method. 
Pay attention to the formatting of the data in the json file. 
Use the 'indent' parameter in the dump() method. Sample result:
"""
movie = {
    "title":"The Fall of the House of Usher",
    "director":"Mike Flanagan",
    "year": 2023,
    "actor":{"leading":"Carla Gugino","supporting":"Kate Siegel"},
    "oscar":False,
    "genre":["Drama","Horror","Mystery"],
    "filming location":"Canada"
}
import json
file = open("favourite.json", "w")
json.dump(movie, file, indent = 4)