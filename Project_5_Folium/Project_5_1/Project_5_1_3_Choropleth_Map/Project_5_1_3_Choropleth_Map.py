# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 17:57:31 2019

@author: dell
"""
import folium
import pandas as pd

# VISUALIZING GEOSPATIAL DATA WITH PYTHON
country_geo = r'E:\\Study\\Project_5_Folium\\Project_5_1\\Project_5_1_3_Choropleth_Map\\world-countries.json'
# Reading and exploring in the database
data = pd.read_csv(r'E:\\Study\\Project_5_Folium\\Project_5_1\\Project_5_1_3_Choropleth_Map\\Indicators.csv')
data.shape
data.head()

# Selecting Life expectancy for females for all countries in 2013
hist_indicator = 'Life expectancy at birth'
hist_year = 2013

mask1 = data['IndicatorName'].str.contains(hist_indicator) 
mask2 = data['Year'].isin([hist_year])

# Applying our mask
stage = data[mask1 & mask2]
stage.head()


# SETTING DATA FOR PLOTTING
#Creating a data frame with just the country codes and the values we want plotted.
data_to_plot = stage[['CountryCode','Value']]
data_to_plot.head()

# Labelling the legend
hist_indicator = stage.iloc[0]['IndicatorName']


# Setup a folium map at a high-level zoom
map = folium.Map(location=[0, 0], zoom_start=1.5)

# choropleth maps bind Pandas Data Frames and json geometries.
#This allows us to quickly visualize data combinations
map.choropleth(geo_data=country_geo, data=data_to_plot,
             columns=['CountryCode', 'Value'],
             name = 'choropleth',
             key_on='feature.id',
             fill_color = 'BuPu', fill_opacity=0.7, line_opacity=0.2,
             legend_name = 'Life expectancy at birth')

folium.LayerControl().add_to(map)

map.save('E:\\Study\\Project_5_Folium\\Project_5_1\Project_5_1_3_Choropleth_Map\\Project_5_1_3_Choropleth_Map.html')

from IPython.display import HTML
HTML('<iframe src=Project_5_1_3_Choropleth_Map.html width=700 height=450></iframe>')