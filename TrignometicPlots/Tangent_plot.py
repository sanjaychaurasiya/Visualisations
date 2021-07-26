import math
import numpy
import matplotlib.pyplot as plt


n = 4    # By changing the value of n the size of graph on x-axis will increase.
input_values = numpy.linspace(-n * math.pi, n * math.pi, 1000)
output_values = [math.tan(value) for value in input_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
plt.plot(input_values, output_values, linewidth=3)
plt.ylim(-15, 15)   # this function is used to increase the size of the plot on y axis.

# Set Graph title and labels.
ax.set_title("Tangent Graph", fontsize=24)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Tangent of Values', fontsize=14)

# Set the tick params.
ax.tick_params(axis='both', labelsize=15)
plt.legend(['tan(x)'])

plt.show()