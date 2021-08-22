import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an api call and store the responses.
url = 'https://corona.lmao.ninja/v2/countries?yesterday&sort'
r = requests.get(url)
print(f'Status Code {r.status_code}')

# Process the requests.
response_dict = r.json()
"""print(response_dict[0])
print(len(response_dict))"""

todayCases, flags, labels = [], [], []
for i in range(len(response_dict)):
    n = response_dict[i]
    todayCase = n['todayCases']
    if todayCase > 1000/2:
        name = n['country']
        todayRecovered = n['todayRecovered']
        test = n['tests']
        active = n['active']
        country_url = n['countryInfo']['flag']
        country_link = f"<a href='{country_url}'>{name}</a>"
        label = f"Name =  {name}<br />TodayCases =  {todayCase}<br />TodayRecovered =  {todayRecovered}<br />" \
                f"Active =  {active}<br />Tests =  {test}"
        todayCases.append(todayCase)
        flags.append(country_link)
        labels.append(label)

# Make visualisations.
data = [{
    'type': 'bar',
    'x': flags,
    'y': todayCases,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(160, 10, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]

my_layout = {
    'title': "Today's Corona Virus Cases",
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Country Name',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': "Today's Cases",
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='corona_virus_today_cases.html')
