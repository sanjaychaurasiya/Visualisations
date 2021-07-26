import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [value**3 for value in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)

# Set chart title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cubes of Values", fontsize=14)

# Set the size of tick parameters.
ax.tick_params(axis='both', labelsize=15)

plt.show()