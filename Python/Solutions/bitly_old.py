"""
Code Challenge
  Name: 
    URL shortening service Bitly
  Filename: 
    bitly.py
  Problem Statement:
In 2011, URL shortening service Bitly partnered with the US government website
USA.gov to provide a feed of anonymous data gathered from users who shorten links
ending with .gov or .mil. In 2011, a live feed as well as hourly snapshots were available
as downloadable text files. This service is shut down at the time of this writing (2017),
but we preserved one of the data files.
In the case of the hourly snapshots, each line in each file contains a common form of
web data known as JSON. (Use example.txt file from Resources)

    Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords
    Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas
    Count the number of occurrence for each time-zone
    Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)
    From field 'a' which contains browser information and separate out browser capability(i.e. the first token in the string eg. Mozilla/5.0)
    Count the number of occurrence for separated browser capability field and plot bar graph for top 5 values (using Seaborn)
    Add a new Column as 'os' in the dataset, separate users by 'Windows' for the values in  browser information column i.e. 'a' that contains "Windows" and "Not Windows" for those who don't

"""

from collections import Counter
import pandas as pd
import numpy as np

data = pd.read_json("example.txt",lines=True)

# Handling missing data
data['tz'] = data['tz'].fillna('Missing')
data['tz'][data['tz'] == ''] = 'Unknown'
# get the most occuring time-zone (with Pandas)
time_zone = data["tz"].value_counts()
print (time_zone.keys()[:10])

# get the most occuring time-zone (without Pandas)
tz = dict(Counter(data['tz']))
tz = [(v,k) for k,v in tz.items()]
tz.sort()
tz.reverse()
key=[tz[i][1] for i in range(len(tz))]
val=[tz[i][0] for i in range(len(tz))]
tz_new = pd.Series(val, index=key)[:10]
print (tz_new)

# display tz output
import seaborn as sb
subset = time_zone[:10]
sb.barplot(y = subset.index, x = subset.values)

# separating browser capability from 'a'
res = pd.Series(i.split()[0] for i in data.a.dropna())
sub_res = res.value_counts()[:5]
sb.barplot(y = sub_res.index, x = sub_res.values)

# separate users by OS
new_os = data[data.a.notnull()]

# Adding os column to classify users as Windows and Not Windows
new_os['os'] = np.where(new_os['a'].str.contains('Windows'),'Windows', 'Not Windows')