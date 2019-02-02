# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 15:28:18 2019

@author: dell
"""

# Importing Libraries
import folium
import pandas as pd

world = folium.Map(location=[100, 0], zoom_start=1.5)

from IPython.display import HTML
HTML('<iframe src=Project_5_1_Stamen_Terrain.html width=700 height=450></iframe>')

# India's Lat and Log and zoom with Stamen Terrain
world = folium.Map(location=[20.5937, 78.9629], zoom_start=4, tiles='Stamen Terrain')
world.save('E:\\Study\\Project_5_Folium\\Project_5_1\\Project_5_1_1_Introduction_to_Folium\\Project_5_1_Stamen_Terrain.html')