washing_product = "underwear"
rinse = True
spin = True
total_time = 0
if washing_product == "shoes":
    total_time += 20
    if rinse == True:
        total_time += 15
    if spin == True:
        total_time += 9
if washing_product == "jacket":
    total_time += 40
    if rinse == True:
        total_time += 15
    if spin == True:
        total_time += 9
if washing_product == "underwear":
    total_time += 70
    if rinse == True:
        total_time += 15
    if spin == True:
        total_time += 9
print(f"Total washing time: {total_time} minutes")