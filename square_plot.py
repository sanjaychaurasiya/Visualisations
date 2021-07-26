import matplotlib.pyplot as plt

x_values = range(1, 51)
y_values = [value**2 for value in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=3)

# Set chart title and labels.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Squares of values", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()