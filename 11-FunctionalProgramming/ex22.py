"""
22.	The array below contains employee data: 
[("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
 ("Jackson","Peter"),("Johnson","Rick"),
 ("Lewis","Terry"),("Clarke","Robin")]
Write a program that determines and displays a list of employees whose last names 
are given in capital letters followed by first names, separated by commas. Sample result:
SMITH, Lucy
JONES, Janet
…
"""
data = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),("Jackson","Peter"),("Johnson","Rick"),("Lewis","Terry"),("Clarke","Robin")]
result = list(map(lambda names: names[0].upper()+", "+names[1],data))
for n in result:
    print(n)