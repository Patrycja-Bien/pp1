#8.	Create a dictionary describing your mobile phone. 
#Use at least 6 key-value pairs of data of different types. 
#Then, using 'for' loop, display the contents of the dictionary. 
#To read a key and value, use the items() method. Sample result:

mobile = {
    "OS":"IOS",
    "Water resistant":True,
    "Color":["Black", "Grey"],
    "Memory":256,
    "Pretty":True,
    "Brand":"Apple"
}
for key,value in mobile.items():
    print(f"{key} : {value}")
