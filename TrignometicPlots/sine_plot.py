import math
import numpy
import matplotlib.pyplot as plt


n = 8    # By increasing the value of n the graph length on x-axis will increase.
input_values = numpy.arange(0, n*numpy.pi, 0.001)
output_values = [math.sin(value) for value in input_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(input_values, output_values, linewidth=3)

# Set the graph title and labels.
ax.set_title("Sine Graph", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Sine of Values", fontsize=14)

# Set tick params.
ax.tick_params(axis='both', labelsize=15)
plt.legend(['sin(x)'])

plt.show()