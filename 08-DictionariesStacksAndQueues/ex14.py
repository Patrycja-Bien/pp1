"""
14.	A dictionary contains course names along with the number of hours. 
Write a program that calculates and displays the total number of hours. Sample results:
winter_semester = {
    "math":60,
    "programming":30,
    "history":15
}
"""
winter_semester = {
    "math":60,
    "programming":30,
    "history":15
}
sum = 0
for i in winter_semester.values():
    sum += i

print("Hours: ",sum)