import matplotlib.pyplot as plt

x_values = range(1, 50001)
y_values = [value for value in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=15)

# Set graph title and label axes.
ax.set_title("Linear Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel('Values', fontsize=14)

# Set tick parameters.
ax.tick_params(axis='both', labelsize=15)

plt.show()