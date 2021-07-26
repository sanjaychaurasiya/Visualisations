import matplotlib.pyplot as plt
import math


input_values = range(2, 1000)
output_values = [math.log(value) for value in input_values]
output_values1 = [1/math.log(value) for value in input_values]

plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
# ax.scatter(input_values, output_values, c=output_values, cmap=plt.cm.Reds, s=15)
# ax.scatter(input_values, output_values1, c=output_values, cmap=plt.cm.Greens, s=15)
ax.plot(input_values, output_values, input_values, output_values1, linewidth=3)
plt.ylim(-0, 7)

# Set the graph label and title.
ax.set_title("Logarithmic and Exponential Graph", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Logarithm and Inverse of Logarithm of values", fontsize=14)

# Set tick parameters.
ax.tick_params(axis='both', labelsize=15)
plt.legend(['log(x)', 'exponential(x)'])

plt.show()