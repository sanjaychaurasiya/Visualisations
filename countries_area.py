import requests

from plotly.graph_objs import bar
from plotly import offline

# Make an api and store the information.
url = 'https://restcountries.eu/rest/v2/all'

r = requests.get(url)
print(f"Status code: {r.status_code}")

# Store api response in a variable.
response_dict = r.json()

names, areas, labels = [], [], []
for i in range(len(response_dict)):
    n = response_dict[i]
    name = n['name']
    names.append(name)
    area = n['area']
    areas.append(area)
    capital = n['capital']
    population = n['population']
    currencie = n['currencies'][0]['name']
    language = n['languages'][0]['name']
    label = f'Name =  {name}<br />Population =  {population}<br />Capital =  {capital}<br />' \
            f'Area =  {area}<br />Currencie =  {currencie}<br />Language =  {language}'
    labels.append(label)

# Make visualisation.
data = [{
    'type': 'bar',
    'x': names,
    'y': areas,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 50)',
        'line': {'width': 1, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.7
}]

my_layout = {
    'title': 'Countries and their Areas.',
    'titlefont': {'size': 24},
    'xaxis': {
        'title': 'Name of the Countries.',
        'titlefont': {'size': 14},
        'tickfont': {'size': 8},
    },
    'yaxis': {
        'title': 'Area',
        'titlefont': {'size': 14},
        'tickfont': {'size': 8},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='CountriesNameAndTheirPopulation.html')