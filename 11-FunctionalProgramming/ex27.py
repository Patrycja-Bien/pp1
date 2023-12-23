"""
27.	Students obtained the following test results (in points, from 0 to 100):
test_results = [
    {"name":"Peter","result":27},
    {"name":"Anna","result":63},
    {"name":"Robert","result":92},
    {"name":"Paul","result":46},
    {"name":"Barbara","result":52}]
Write a program that displays students whose scores are between 50 and 70 points. 
Use an anonymous function and filter() function.
"""
test_results = [
    {"name":"Peter","result":27},
    {"name":"Anna","result":63},
    {"name":"Robert","result":92},
    {"name":"Paul","result":46},
    {"name":"Barbara","result":52}]

result = list(filter(lambda student: 50 <= student["result"] <= 70,test_results))
print(result)
