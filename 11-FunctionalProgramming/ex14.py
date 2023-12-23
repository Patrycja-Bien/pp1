"""
14.	The report below shows the last five credit card payments in Euro:
15.90
38.47
4.07
132.70
9.15
Write a program that calculates and displays transaction amounts in Polish zlotys 
(1 EUR = 4.5 PLN). Use anonymous and map() functions. Sample result:
"""
eur = [15.90,38.47,4.07,132.70,9.15]
pln = list(map(lambda x:x*4.5, eur))
# print pln list ...
for i in pln:
    print(round(i,2))