speed = input("Enter vehicle speed: ")
speed = int(speed)
check = (speed >= 40) and (speed <= 140)
print(f"Speed is valid: {check}")