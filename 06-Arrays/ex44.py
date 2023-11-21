import matplotlib.pyplot as plt

x = []
y = []
def f(x):
    return x**2 - 3
# create x values
for n in range(-100,101):
    x.append(n)

# create y values
for n in x:
    y.append(f(n))

# display chart
plt.plot(x, y)
plt.show()