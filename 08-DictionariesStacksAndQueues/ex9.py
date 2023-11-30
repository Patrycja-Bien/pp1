"""
9.	Create an array with 5 dictionaries, each containing a country and its population. 
Then, using a ‘while’ loop, display the array contents. Sample result:
countries = [
    {"name":"Poland", "population":38000000},
    …
    …
    …
    …
]
COUNTRY  POPULATION
Poland   38000000
…        …
…        …
…        …
…        …

"""
countries = [
    {"name":"Poland", "population":18000000},
    {"name":"UK", "population":2309138293829},
    {"name":"USA", "population":382983298938239928393},
    {"name":"Australia", "population":49302930293093},
    {"name":"Germany", "population":555555555}
]
x = 0
print("COUNTRY","   ","POPULATION")
while x < len(countries):
    print(countries[x]["name"],"    ",countries[x]["population"])
    x+=1