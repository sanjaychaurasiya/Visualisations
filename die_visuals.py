from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a die with side 6.
die = Die()

# Make some roll and store the results in a list.
results = []
for roll_number in range(10000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise the results.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_configuration = {'title': 'Result'}
y_axis_configuration = {'title': 'Frequency of Result'}
my_layout = Layout(title='Result of rolling one D6 1000 times', xaxis=x_axis_configuration, yaxis=y_axis_configuration)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
