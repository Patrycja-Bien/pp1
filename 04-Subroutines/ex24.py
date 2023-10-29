import range

number = int(input("Enter number: "))
range1 = int(input("Enter min value: "))
range2 = int(input("Enter max value: "))

result = range.range(number,range1,range2)
if result == True:
    result = "Yes"
else:
    result = "No"
print(f"Number {number} in the range <{range1},{range2}>: {result}")