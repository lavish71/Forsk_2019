# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:38:27 2019

@author: dell
"""

# Importing required libraries
import matplotlib.pyplot as plt
# To import the basemap library give the direct path to the library
import os
os.environ["PROJ_LIB"]="C:\\ProgramData\\Anaconda3\\Library\\share"
from mpl_toolkits.basemap import Basemap
import geopandas as gpd
import pandas as pd


city=gpd.read_file("E:\\Study\\Project_1_Basic_Libraries\\Project_1_3_Basemap\\District_boundary\\District_Boundary.shp")
csv=pd.read_csv("E:\\Study\\Project_1_Basic_Libraries\\Project_1_3_Basemap\\latlong_raj.csv")


lat=csv['LAT'].values
lon=csv['LONG'].values
population = city['POPULATION'].values
dist=city['DIST_NAME'].values


fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution='h', 
            lat_0=27.0238, lon_0=74.2179,
            width=1.05E6, height=1.2E6)
m.shadedrelief()


m.drawcoastlines(color='blue',linewidth=3)
m.drawcountries(color='gray',linewidth=3)
m.drawstates(color='gray')
    

# scatter city data, with c reflecting population
m.scatter(lon,lat, latlon=True,
          c=population,s=700,
          cmap='YlGnBu_r', alpha=0.5)
#create colorbar 
plt.colorbar(label=r'Population')
plt.clim(300000, 4000000)


dict1={}
list1=[]
list2=[]
list3=[]

#storing each value in different lists
for z in lat:
    list1.append(z)
for c in lon:
    list2.append(c)
for b in dist:
    list3.append(b)
#storing the values of lat long in a dictionary with lat as keys and long as values
n=0
while(n<len(list1)):
    dict1[list1[n]]=list2[n]
    n+=1
    
    
i=0
# Map (long, lat) to (x, y) for plotting
#naming the cities of Rajasthan with the help of their lat(z)long(c)
for z,c in dict1.items():
    x,y = m(c, z)
    plt.plot(x, y, 'ok', markersize=5)
    plt.text(x, y,list3[i], fontsize=10);
    i+=1
    
