def computepay(hours, rate):
    
    if hours > 40:
        result = (hours - 40)*(rate*1.5) + 40*rate
    else:
        result = hours*rate
    print(f"Pay: {result}")

computepay(45, 10)

def computegrade(x):
    if x < 0 or x > 1:
        print("Wrong value")
    elif x >= 0.9:
        print("Grade: 5.0")
    elif x >= 0.8:
        print("Grade: 4.5")
    elif x >= 0.7:
        print("Grade: 4.0")
    elif x >= 0.6:
        print("Grade: 3.5")        
    elif x >= 0.5:
        print("Grade: 3.0")
    else:
        print("Grade: 2.0")

computegrade(0.7)