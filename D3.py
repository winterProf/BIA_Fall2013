# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import random
import numpy as np
import pandas as pd
import json
import vincent

# <codecell>

# To allow vincent visualizations within an iPython notebook
vincent.core.initialize_notebook()

# <codecell>

#Iterable
list_data = [10, 20, 30, 20, 15, 30, 45]

# <codecell>

bar = vincent.Bar(list_data)
bar.axis_titles(x='Index', y='Value')
bar.height=300
bar.width=300
bar.display()

# <codecell>

line = vincent.Line(list_data)
line.axis_titles(x='Index', y='Value')
line.height=300
line.width=400
line.display()

# <codecell>

#Dicts of iterables
cat_1 = ['y1', 'y2', 'y3', 'y4']
index_1 = range(0, 21, 1)
multi_iter1 = {'index': index_1}
for cat in cat_1:
    multi_iter1[cat] = [random.randint(10, 100) for x in index_1]

# <codecell>

multi_iter1.keys()

# <codecell>

line = vincent.Line(multi_iter1, iter_idx='index')
line.axis_titles(x='Index', y='Value')
line.legend(title='Categories')
line.colors(brew='Set1')
line.height=300
line.width=600
line.display()

# <codecell>

# Second dictionary of iterables
cat_2 = ['y' + str(x) for x in range(0, 10, 1)]
index_2 = range(1, 21, 1)
multi_iter2 = {'index': index_2}
for cat in cat_2:
    multi_iter2[cat] = [random.randint(10, 100) for x in index_2]

# <codecell>

import pandas.io.data as web
all_data = {}
for ticker in ['AAPL', 'GOOG', 'FB', 'YHOO', 'MSFT']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2010', '1/1/2013')
price = pd.DataFrame({tic: data['Adj Close']
                      for tic, data in all_data.iteritems()})

# <codecell>

price['YHOO']

# <codecell>

line = vincent.Line(price[['FB', 'YHOO']])
line.axis_titles(x='Date', y='Price')
line.legend(title='FB vs YHOO')
line.width=600
line.height=400
line.display()

# <codecell>

area = vincent.Area(list_data)
area.width=600
area.height=400
area.display()

# <codecell>

stacked = vincent.StackedArea(multi_iter1, iter_idx='index')
stacked.axis_titles(x='Index', y='Value')
stacked.legend(title='Categories')
stacked.height=300
stacked.width=600
stacked.display()

# <codecell>

stacked = vincent.StackedArea(price)
stacked.axis_titles(x='Date', y='Price')
stacked.legend(title='Tech Stocks')
#stacked.colors(brew='Spectral')
#stacked.colors(brew='Accent')
stacked.height=300
stacked.width=600
stacked.display()

# <codecell>

farm_1 = {'apples': 10, 'berries': 32, 'squash': 21, 'melons': 13, 'corn': 18}
farm_2 = {'apples': 15, 'berries': 43, 'squash': 17, 'melons': 10, 'corn': 22}
farm_3 = {'apples': 6, 'berries': 24, 'squash': 22, 'melons': 16, 'corn': 30}
farm_4 = {'apples': 12, 'berries': 30, 'squash': 15, 'melons': 9, 'corn': 15}

farm_data = [farm_1, farm_2, farm_3, farm_4]
farm_index = ['Farm 1', 'Farm 2', 'Farm 3', 'Farm 4']
df_farm = pd.DataFrame(farm_data, index=farm_index)

# <codecell>

group = vincent.GroupedBar(df_farm)
group.axis_titles(x='Total Produce', y='Farms')
group.legend(title='Produce Types')
group.colors(brew='Set1')
group.width=600
group.height=400
group.display()

# <codecell>

world_topo = r'world-countries.topo.json'
geo_data = [{'name': 'countries',
             'url': world_topo,
             'feature': 'world-countries'}]

vis = vincent.Map(geo_data=geo_data, scale=200)
vis.to_json('map.json', html_out=True, html_path='map_template.html')

# <codecell>

#Map Data Binding
#Map the county codes we have in our geometry to those in the
#county_data file, which contains additional rows we don't need
with open('us_counties.topo.json', 'r') as f:
    get_id = json.load(f)

# <codecell>

#A little FIPS code munging
new_geoms = []
for geom in get_id['objects']['us_counties.geo']['geometries']:
    geom['properties']['FIPS'] = int(geom['properties']['FIPS'])
    new_geoms.append(geom)

get_id['objects']['us_counties.geo']['geometries'] = new_geoms

with open('us_counties.topo.json', 'w') as f:
    json.dump(get_id, f)

#Grab the FIPS codes and load them into a dataframe
geometries = get_id['objects']['us_counties.geo']['geometries']
county_codes = [x['properties']['FIPS'] for x in geometries]
county_df = pd.DataFrame({'FIPS': county_codes}, dtype=str)
county_df = county_df.astype(int)

#Read into Dataframe, cast to string for consistency
df = pd.read_csv('us_county_data.csv', na_values=[' '])
df['FIPS_Code'] = df['FIPS'].astype(str)

#Perform an inner join, pad NA's with data from nearest county
merged = pd.merge(df, county_df, on='FIPS', how='inner')
merged = merged.fillna(method='pad')

# <codecell>

county_topo = 'us_counties.topo.json'
state_topo = 'us_states.topo.json'

# <codecell>

geo_data = [{'name': 'counties',
             'url': county_topo,
             'feature': 'us_counties.geo'},
            {'name': state_topo,
             'url': 'us_states.topo.json',
             'feature': 'us_states.geo'}]

vis = vincent.Map(geo_data=geo_data, scale=1000, projection='albersUsa')
del vis.marks[1].properties.update
vis.marks[0].properties.update.fill.value = '#084081'
vis.marks[1].properties.enter.stroke.value = '#fff'
vis.marks[0].properties.enter.stroke.value = '#7bccc4'

# <codecell>

geo_data = [{'name': 'counties',
             'url': county_topo,
             'feature': 'us_counties.geo'}]

vis = vincent.Map(data=merged, geo_data=geo_data, scale=1100, projection='albersUsa',
          data_bind='Employed_2011', data_key='FIPS',
          map_key={'counties': 'properties.FIPS'})
vis.marks[0].properties.enter.stroke_opacity = vincent.ValueRef(value=0.5)
vis.to_json('vega.json', html_out=True, html_path='map_template.html')

# <codecell>


