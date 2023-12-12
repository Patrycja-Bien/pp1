"""
20.	The website http://api.nbp.pl contains data on exchange 
rates published by the National Bank of Poland. 
The service provides data in json or xml formats. 
Display the last ten Euro exchange rates in json format in the browser window. 
Save the data to the euro.json file. Then, write a program that 
displays the data from the euro.json file in the following format:
Date            Buying Rate     Selling Rate
============================================
2019-10-25      3.8150          3.9820
...             ...             ...
"""
import json
with open("euro.json","r") as file:
    data = json.load(file)
    header = "Date              Buying Rate             Selling Rate"
    print(header)
    print("="*len(header))
    for rate in data['rates']:
        date = rate['effectiveDate']
        buying_rate = rate['bid']
        selling_rate = rate['ask']
        result = f"{date}           {buying_rate}               {selling_rate}"
        print(result)
