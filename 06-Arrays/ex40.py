import random
arr = [random.randint(1,999) for i in range(8)]
x = (5*len(arr) + 1)*"-"
y = "|".join(["{:4}".format(num) for num in arr])
table = f"{x}\n|{y}|\n{x}"

print(table)