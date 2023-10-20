import random

result = ""
result = list(result)

for i in range(20):
    number = random.randint(5, 10)
    result.append(number)

print("20 random numbers:"," ".join(str(x) for x in result))