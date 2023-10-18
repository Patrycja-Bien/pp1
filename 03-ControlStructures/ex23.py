age = input("Enter the dog's age in human years: ")
age = float(age)

if age <= 2:
    age = age * 10.5
else:
    age = (age - 2) * 4 + 21
print(f"The dog's age in dog's years is {age} years.")