cm = input("Enter your height in cm: ")
cm = float(cm)
m = cm / 100
kg = input("Enter your weight in kg: ")
kg = float(kg)
bmi = kg / m**2
bmi = round(bmi, 1)
healthy = (bmi >= 18.5) and (bmi <= 24.9)
print(f"Your BMI index: {bmi}")
print(f"Correct weight: {healthy}")