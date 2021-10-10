#!/usr/bin/env python
# coding: utf-8

# # Installation instructions
# 
# ## From an ALP lab computer
# * Open Anaconda Navigator
# * Click on Environments (left side)
# * Change the dropdown menu from "Installed" to "All" (it might already be on "All")
# * Search Packages for "Altair"
# * Click the checkbox next to Altair (if it already shows a green checkbox, then it's already installed)
# * Click "Apply" at the bottom
# * Wait
# * Switch back from "Environments" to "Home"
# * Open Jupyter Notebook
# 
# ## From your own computer
# If you're lucky, this is as easy as running `pip install altair` (for example, on a Mac you can try running this command in Terminal).
# 
# If that doesn't work, another option is to use Anaconda Navigator from your own computer.  Try the above steps.  If they do not work (because Altair does not show up at all when you search), then open a Terminal from within Anaconda Navigator, and run `pip install altair`.
# 
# Altair is just one of many plotting libraries.  It is my favorite, but it is definitely not the most famous.  It might not even be the fifth most famous.  In Math 10, will also use Matplotlib and Seaborn.  Some others, that we probably will not use, are Plotly and Holoviews (actually Holoviews probably isn't technically a plotting library, but let's ignore that).

# In[1]:


# If you see ModuleNotFoundError: No module named 'altair'
# then you have not yet installed Altair.
# Follow the steps above, or an alternative like pip install altair

import altair as alt
import pandas as pd
import numpy as np
rng = np.random.default_rng()


# ## Basic example with random data
# The syntax for Altair can be intimidating the first time you see it (and the fifth time you see it).  Here is some information.  Skip this information for now, and come back to it when you need it.
# * Options for what to draw: [Marks](https://altair-viz.github.io/user_guide/marks.html)
# * Different "channels", like `color`, `opacity`, and `size`.  You can see a list of channels here: [Documentation](https://altair-viz.github.io/user_guide/encoding.html#encoding-channels).
# * Here is a list of color schemes: [Vega color schemes](https://vega.github.io/vega/docs/schemes/) and an [example](https://altair-viz.github.io/user_guide/customization.html#color-schemes) of how to use a color scheme in Altair.
# * Sometimes it helps to explicitly tell Altair what type of data it is: [encoding types](https://altair-viz.github.io/user_guide/encoding.html#encoding-data-types)
# * If you find browsing examples easier than reading documentation, check out the Altair [example gallery](https://altair-viz.github.io/gallery/index.html)

# In[2]:


# Making some data
A = rng.integers(0,100,size = (6000,4))
rand_df = pd.DataFrame(A, columns = ["a","b","c","d"])


# In[3]:


rand_df


# In[4]:


alt.Chart(rand_df.iloc[:5000]).mark_circle().encode(
    x = "a",
    y = "b"
)


# ## Example with data from Spotify
# Download the `spotify_dataset.csv` file from Canvas, and put it somewhere you can access from Jupyter (maybe in the same folder as this notebook).
# 
# The dataset originally came from Kaggle [here](https://www.kaggle.com/sashankpillai/spotify-top-200-charts-20202021).  You can go there to see a description of the columns.

# In[5]:


# Change the path if necessary
# Doing some small "data cleaning": converting some columns from strings to numbers.
df = pd.read_csv("spotify_dataset.csv")
df = df.replace(" ",np.nan)
df["Streams"] = df["Streams"].str.replace(",","")
df.iloc[:,[5,7]] = df.iloc[:,[5,7]].apply(pd.to_numeric,axis=0).copy()
df.iloc[:,12:22] = df.iloc[:,12:22].apply(pd.to_numeric,axis=0).copy()


# In[6]:


df.dtypes


# In[7]:


alt.Chart(df).mark_circle().encode(
    x = "Energy",
    y = "Loudness",
    color = alt.Color('Energy', scale=alt.Scale(scheme='turbo')),
    tooltip = ["Song Name", "Artist"]
).properties(
    width = 400
)


# In[8]:


df[df["Loudness"] < -20]


# In[9]:


df.sort_values("Loudness", ascending=False)


# In[ ]:




