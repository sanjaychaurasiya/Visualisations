import matplotlib.pyplot as plt


input_values = range(-100, 100)
output_values = []
output_values1 = []
for value in input_values:
    value = 1
    output_values.append(value)
    value = -1
    output_values1.append(value)

plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(output_values, input_values, output_values1, input_values, linewidth=3)
plt.ylim(-4, 4)

# Set title and labels for the graph.
ax.set_title('Line parallel to y-axis', fontsize=24)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Value of y', fontsize=14)

# Set tick parameters.
ax.tick_params(axis='both', labelsize=15)
plt.legend(['x = 1', 'x = -1'])

plt.show()
