car_speed = int(input("Enter car speed: "))
speed_limit_min = 40
speed_limit_max = 140
if car_speed > speed_limit_min and car_speed < speed_limit_max:
    print("Speed valid")
else:
    print("Warning: invalid car speed!!")