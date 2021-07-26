import matplotlib.pyplot as plt

x_values = range(1, 501)
y_values = [1 / value for value in x_values]

plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=3)

# Set chart title and labels.
ax.set_title('Inverse Function', fontsize= 24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Inverse of value', fontsize=14)

# Set the size of tick params.
ax.tick_params(axis='both', which='major', labelsize=15)

plt.show()