import matplotlib.pyplot as plt
import math


input_values = range(-10, 10)
output_values = [math.exp(value) for value in input_values]
output_values1 = [1/math.exp(value) for value in input_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(input_values, output_values, input_values, output_values1, linewidth=3)
plt.ylim(-1, 45)

# Set the title and labels for the graph.
ax.set_title('Exponential Function Graph', fontsize=24)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Values of y', fontsize=14)

# Set tick parameters.
ax.tick_params(axis='both', labelsize=15)
plt.legend(['exponential(x)', '1/exponential(x)'])

plt.show()
