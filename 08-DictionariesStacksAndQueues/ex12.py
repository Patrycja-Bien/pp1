"""
12.	Write a program in which you create a dictionary containing student data. 
Try to describe a student in detail, using different data types that can be used in the dictionary. 
Then, save the data about student in the file student.json, in a readable form.
"""
student = {
    "name":"Drew",
    "surname":"Gooden",
    "age":22,
    "gender":"male",
    "full-time student":True,
    "hobby":["swimming","dancing","video games"]
}
import json
file = open("student.json", "w")
json.dump(student,file,indent = 6)
