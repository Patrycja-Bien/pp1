t = (50,20,40,50,30,50)
v = int(input("Enter number: "))
o = t.count(v)

print("Tuple:"," ".join(str(i) for i in t))
print("Value:", v)
print("Number of occurences: ", o)