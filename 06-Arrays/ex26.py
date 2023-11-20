x = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

max = ""

for name in x:
    if len(max) < len(name):
        max = name

print(f"Names: {" ".join(str(i) for i in x)}")
print(f"Longest name: {max}")