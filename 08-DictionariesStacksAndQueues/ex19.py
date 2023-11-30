"""
19.	Using the website https://mockaroo.com, generate a list of 500 students, 
containing the following data: name, surname, student ID, gender, age, year of study, email. 
Write the data to the students.json file. 
Then, write a program that creates the limited.json file containing 
the list of students limited to data: first name, last name, student id.
"""
import json
with open("students.json","r") as file:
    students = json.load(file)
    new_file = open("limited.json", "w")
    limited = ["name", "surname", "id"]
    limited_data = [{field: student[field] for field in limited} for student in students]
    json.dump(limited_data, new_file, indent = 2)

