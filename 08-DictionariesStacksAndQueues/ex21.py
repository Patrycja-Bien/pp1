"""
21.	The products.csv file contains data about the products sold. 
Create the file in a text editor.
Product,Quantity,Price
milk,8,4.25
cheese,5,17.90
bread,21,6.15
juice,12,5.90
Then, write a program to convert data from CSV to JSON. 
The program reads product data from the CSV file and writes the data to a JSON file.
"""
import csv
import json

with open("products.csv","r") as file:
    data = csv.DictReader(file)
    result = []
    for row in data:
        result.append(row)
    new_file = open("products.json","w")
    json.dump(result,new_file,indent=2)
