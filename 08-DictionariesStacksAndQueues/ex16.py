"""
16.	A program contains two functions:
a.	hotel_list(hotels) that returns a list of hotels names, separated by a comma sign
b.	avg_price(hotels) that returns the average room price for a given list of hotels, 
rounded to an integer value
c.	Write a program that calculates and displays the average price for a room 
in hotels in Krakow and Sopot and indicates in which cities hotels are cheaper.
Sample result:
Hotels in Krakow: …,…,…,…
Average hotel price in Krakow: …
Hotels in Sopot: …,…,…,…
Average hotel price in Sopot: …
Cheaper hotels in: …
"""
Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    result = []
    for i in hotels:
        result.append(i["name"])
    return ",".join((i) for i in result)

def avg_price(hotels):
    sum = 0
    count = len(hotels)
    for i in hotels:
        sum += i["price"]
    return int(sum/count)

def where_cheaper():
    if avg_price(Hotels_in_Krakow) < avg_price(hotels_in_Sopot):
        return "Krakow"
    else:
        return "Sopot"
    
print(f"Hotels in Krakow: {hotel_list(Hotels_in_Krakow)}")
print(f"Average hotel price in Krakow: {avg_price(Hotels_in_Krakow)}")
print(f"Hotels in Sopot: {hotel_list(hotels_in_Sopot)}")
print(f"Average hotel price in Sopot: {avg_price(hotels_in_Sopot)}")
print(f"Cheaper hotels in: {where_cheaper()}")