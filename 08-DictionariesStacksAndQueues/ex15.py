"""
15.	The program contains two dictionaries with personal data:
Write a program that creates a dictionary called ‘person’ 
containing data from the two given dictionaries (five key-value pairs). 
Display the contents of the ‘person’ dictionary.
"""
basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}
person = basic_data.copy()
person.update(advanced_data.items())
print(person)