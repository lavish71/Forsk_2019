# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 17:08:21 2019

@author: dell
"""

# Importing Libraries
import os
os.environ["PROJ_LIB"]="C:\\ProgramData\\Anaconda3\\Library\\share"
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


# DRAWING THE FIRST MAP
# Simplest Map
map = Basemap()

map.drawcoastlines()

plt.show()


# Projection with some customisation
map = Basemap(projection='ortho', 
              lat_0=50, lon_0=10)

#Fill the globe with a blue color 
map.drawmapboundary(fill_color='aqua')
#Fill the continents with the land color
map.fillcontinents(color='coral',lake_color='aqua')

map.drawcoastlines()

plt.show()


# MANAGING PROJECTIONS
# Passing the bounding box
map = Basemap(llcrnrlon=-10.5,llcrnrlat=35,urcrnrlon=4.,urcrnrlat=44.,
             resolution='i', projection='tmerc', lat_0 = 39.5, lon_0 = -3.25)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

plt.show()


# Passing the bounding box in the map coordinates
map = Basemap(resolution='l', 
              satellite_height=3000000.,
              projection='nsper', 
              lat_0 = 30., lon_0 = -27.,
              llcrnrx=500000.,llcrnry=500000.,urcrnrx=2700000.,urcrnry=2700000.
             )

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

plt.show()


# Passing the center, width and height
map = Basemap(projection='aeqd',
              lon_0 = 0,
              lat_0 = 90,
              width = 10000000,
              height = 10000000)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

for i in range(0, 10000000, 1000000):
    map.plot(i, i, marker='o',color='k')

plt.show()


# BASIC FUNCTIONS
# Drawing a point in a map
map = Basemap(projection='ortho',
              lat_0=0, lon_0=0)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral', lake_color='aqua')
map.drawcoastlines()

x,y = map(0, 0)

map.plot(x, y, marker='o', color='m')

plt.show()


# Drawing more than one point in a map
map = Basemap(projection = 'ortho',
              lat_0=0, lon_0=0)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral', lake_color='aqua')
map.drawcoastlines()

lons = [0, 10, -20, -20]
lats = [0, -10, 40, -20]

x,y = map(lats, lons)

map.scatter(x, y, marker='D', color='m')

plt.show()


