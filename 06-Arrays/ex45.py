import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 360 degrees
x = np.arange(0, 361, 1)

# Convert degrees to radians for the sine function
y = np.sin(np.radians(x))

# Plot the sine function
plt.plot(x, y)

# Set plot labels and title
plt.xlabel('Angle (degrees)')
plt.ylabel('sin(x)')
plt.title('Plot of y = sin(x)')

# Display the plot
plt.show()
