from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create dice with sides 6 and 8.
die1 = Die()
die2 = Die(8)
die3 = Die(10)

# Make some roll and store the results in a list.
results = []
for roll_number in range(50_000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_results = die1.num_sides + die2.num_sides + die3.num_sides
for value in range(2, max_results + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise the results.
x_values = list(range(2, max_results+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_configuration = {'title': 'Result', 'dtick': 1}
y_axis_configuration = {'title': 'Frequency of Result'}
my_layout = Layout(title='Result of rolling a D6 and a D8 50_000 times', xaxis=x_axis_configuration, yaxis=y_axis_configuration)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d8.html')
