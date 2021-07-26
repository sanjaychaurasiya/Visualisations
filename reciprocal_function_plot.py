import matplotlib.pyplot as plt


input_values = range(-100, 100)
output_values = []
for value in input_values:
    try:
        z = 1/value
    except ZeroDivisionError:
        z = 1
    else:
        output_values.append(z)

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(input_values, output_values, linewidth=3)

# Set title and labels for the graph.
ax.set_title('Inverse Function Graph', fontsize=24)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Values of y', fontsize=14)

# Set tick parameters.
ax.tick_params(axis='both', labelsize=15)

plt.show()