"""
17.	The following people are employed in one of the company's departments:
SMITH Lucy
JONES Janet
LEE Jerry
JACKSON Peter
JOHNSON Rick
LEWIS Terry
CLARKE Robin
Save the list of employees in a string array. Then, write a program that displays people 
whose surnames start with the letter 'J'. Use anonymous and filter() functions. 
Sample result:
employees = ["SMITH Lucy","JONES Janet","LEE Jerry","JACKSON Peter","JOHNSON Rick","LEWIS Terry","CLARKE Robin"]
emp_J = list(filter(lambda e:e[0]=="J", employees))
# print a list … 
...
JONES Janet
JACKSON Peter
JOHNSON Rick
"""
employees = ["SMITH Lucy","JONES Janet","LEE Jerry","JACKSON Peter","JOHNSON Rick","LEWIS Terry","CLARKE Robin"]
emp_J = list(filter(lambda e:e[0]=="J", employees))

for name in emp_J:
    print(name)