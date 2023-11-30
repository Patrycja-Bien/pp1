"""
7.	Create a dictionary as in the example below. 
Note the structure of the dictionary (key-value) and the value types in the example below. 
What type of value was used in each of the six key-value pairs?
"""
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

# Then, create a program that:
# a.	Displays contents of the dictionary
print("A")
print(person)
print()
# b.	Displays name
print("B")
print(person["name"])

print()
# c.	Displays hobby
print("C")
print(" ".join((i) for i in person["hobby"]))
print()
# d.	Changes surname to 'Nowak'
print("D")
person["surname"] = "Nowak"
print(person)
print()
# e.	Changes person's marriage status
print("E")
person["married"] = "False"
print(person)
print()
# f.	Adds gender: 'male'
print("F")
person["gender"] = "male"
print(person)
print()
# g.	Adds a new hobby: 'bicycle'
print("G")
person["hobby"].append("bicycle")
print(person)
print()
# h.	Adds work phone to existing phones: '313131444'
print("H")
person["phone"].update({"work phone":"313131444"})
print(person)