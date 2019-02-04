# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:46:55 2019

@author: dell
"""

# Importing required libraries
import matplotlib.pyplot as plt
# To import the basemap library give the direct path to the library 
import os
os.environ["PROJ_LIB"]="C:\\ProgramData\\Anaconda3\\Library\\share"
from mpl_toolkits.basemap import Basemap
import geopandas as gpd

# Reading shapefile using geopandas
city=gpd.read_file("E:\\Study\\Project_1_Basic_Libraries\\Project_1_3_Basemap\\District_boundary\\District_Boundary.shp")

# Plotting axis using matplotlib
fig = plt.figure(figsize=(8, 8))

# Plotting Map using Basemap
m = Basemap(projection='ortho', resolution='h', 
            lat_0=20.5937, lon_0=78.9629,
            width=8E6, height=8E6)
m.shadedrelief()

# Map (long, lat) to (x, y) for plotting name of country
x, y = m(75, 25)  
plt.plot(x, y, 'ok', markersize=5)
plt.text(x, y, 'India', fontsize=15)