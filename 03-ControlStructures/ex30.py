time24 = input("Enter time (24-hour format): ")
if len(time24) == 5:
    hours = time24[:2]
    minutes = time24[3:]
    hours = int(hours)
    if hours <= 12:
        print(f"Time in 12-hour format: {time24}am")
    else:
        hours -= 12
        print(f"Time in 12-hour format: {hours}:{minutes}pm")
elif len(time24) == 4:
    hours = time24[:1]
    minutes = time24[2:]
    hours = int(hours)
    print(f"Time in 12-hour format: {time24}am")
else:
    print("Wrong time")

