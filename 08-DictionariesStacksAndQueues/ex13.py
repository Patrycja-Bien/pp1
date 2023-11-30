"""
13.	A program contains any defined dictionary, with any number of key-value pairs of information. 
Write a program that displays the number of pairs of information available in the dictionary.
"""
student = {
    "name":"Drew",
    "surname":"Gooden",
    "age":22,
    "gender":"male",
    "full-time student":True,
    "hobby":["swimming","dancing","video games"]
}
print(len(student))