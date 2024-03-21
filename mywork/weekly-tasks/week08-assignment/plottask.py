import matplotlib.pyplot as plt
import numpy as np

# Generate 1000 random values from a normal distribution
mean = 5
std_dev = 2
values = np.random.normal(mean, std_dev, 1000)

# Plot histogram of the normal distribution
plt.hist(values, bins=30, density=True, alpha=0.5, color='blue', label='Normal Distribution')

# Plot the function h(x) = x^3 in the range [0, 10]
x = np.linspace(0, 10, 100)
y = x ** 3
plt.plot(x, y, color='red', label='$h(x) = x^3$')

# Add legend and labels
plt.legend()
plt.xlabel('Value')
plt.ylabel('Frequency/Density')
plt.title('Histogram of Normal Distribution and Function $h(x) = x^3$')

# Show plot
plt.grid(True)
plt.show()
