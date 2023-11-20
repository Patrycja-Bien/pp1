def compare(ar1,ar2):
    if len(ar1) != len(ar2):
        return False
    for i in range(len(ar1)):
        if ar1[i] != ar2[i]:
            return False
    return True

a1 = ["water","book","sky"] 
a2 = ["water","book","sky"]
b1 = [True,False]   
b2 = [True,False,True]
c1 = [5,3,1]   
c2 = [5,3,1]
d1 = [3,2,1]   
d2 = [3,2]

print(f"Array 1: {" ".join(str(i) for i in a1)}")
print(f"Array 2: {" ".join(str(i) for i in a2)}")
if compare(a1,a2) == True:
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are NOT the same")

print(f"Array 1: {" ".join(str(i) for i in b1)}")
print(f"Array 2: {" ".join(str(i) for i in b2)}")
if compare(b1,b2) == True:
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are NOT the same")

print(f"Array 1: {" ".join(str(i) for i in c1)}")
print(f"Array 2: {" ".join(str(i) for i in c2)}")
if compare(c1,c2) == True:
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are NOT the same")

print(f"Array 1: {" ".join(str(i) for i in d1)}")
print(f"Array 2: {" ".join(str(i) for i in d2)}")
if compare(d1,d2) == True:
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are NOT the same")