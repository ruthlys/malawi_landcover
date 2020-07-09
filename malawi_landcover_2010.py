#!/usr/bin/env python
# coding: utf-8

# # Landcover in Malawi (2010) by Malawi Spatial Data Platform (MASDAP)
# 
# <p>Data were obtained from the ArcGIS Hub and provide details of the various types of land cover in Malawi.</p>
# 
# <p>This is an example of how to use plotly express and choropleth mapbox to plot geospatial data.</p>

# In[11]:


# import geojson file from ArcGIS Open Data Hub
from urllib.request import urlopen
import json
with urlopen('https://opendata.arcgis.com/datasets/7533fe68b047461ea6187841c706375b_3.geojson') as response:
    malawi = json.load(response)

# print first 10 features
malawi["features"][10]


# In[12]:


# import df with same object ID from ArcGIS server
import pandas as pd
df = pd.read_csv("Malawi_2016.csv",
                   dtype={"NAME": str})

import geopandas as gpd
# load plotly express
import plotly.express as px

# print head of df
df.head(10)


# In[13]:


df.info()


# In[14]:


# plot histogram of type of landcover
fig = px.pie(df, values = "OBJECTID", names="NAME", title = "Type of land cover in Malawi (2016)")
fig.show()


# In[15]:


#plot histogram of sum hectare per land use area
fig = px.histogram(df, x="NAME", y="HECTARES").update_xaxes(categoryorder="total descending")

fig.update_layout(
    title={
        'text': "Sum of hectares per land use area (2016)",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_yaxes(showgrid=False)  # turning off the grid
fig.show()


# In[ ]:


fig = px.choropleth_mapbox(df, geojson=malawi, color="NAME",
                           locations="HECTARES", featureidkey="properties.HECTARES",
                           center={"lat": -13.254308, "lon": 34.301525},
                           mapbox_style="carto-positron", zoom=9)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[ ]:




