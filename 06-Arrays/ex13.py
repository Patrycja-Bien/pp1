import matplotlib

import matplotlib.pyplot as plt

data = {"car":25, "public transport":19, "bike":32,"on foot":7}

transport = list(data.keys())
values = list(data.values())

plt.bar(transport, values, color ="pink", width = 0.5)

plt.xlabel("Modes of transportation")
plt.ylabel("Number of employees")
plt.title("Wykres")
plt.show()