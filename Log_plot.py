import matplotlib.pyplot as plt
import math


input_values = range(1, 1000)
output_values = [math.log(value) for value in input_values]

plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.scatter(input_values, output_values, c=output_values, cmap=plt.cm.Reds, s=15)

# Set the graph label and title.
ax.set_title("Logarithmic Graph", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Logarithm of values", fontsize=14)

# Set tick parameters.
ax.tick_params(axis='both', labelsize=15)

plt.show()