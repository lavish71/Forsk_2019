# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 16:25:38 2019

@author: dell
"""

# Importing Libraries
import folium
import pandas as pd

map = folium.Map(location=[26.7888, 75.8273], zoom_start=15)

mark = folium.map.FeatureGroup()

mark.add_child(
        folium.CircleMarker(
                [26.788883,75.827338], radius = 20,
                color = "green", fill_color = "Red"))

mark.add_child(folium.Marker(
        [26.788883,75.827338], 
        popup = "Forsk Technologies"))

map.add_child(mark)

map.save('E:\\Study\\Project_5_Folium\\Project_5_1\\Project_5_1_2_Marker\\Project_5_1_2_Marker.html')


