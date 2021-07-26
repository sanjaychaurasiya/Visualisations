import matplotlib.pyplot as plt

x_values = range(1, 501)
y_values = [value**2 for value in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=20)

# Set title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Squares of Values", fontsize=14)

# Set the size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=15)

plt.show()
