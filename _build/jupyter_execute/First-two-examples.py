#!/usr/bin/env python
# coding: utf-8

# # First two examples of Altair Charts
# We give two examples, one produced with random data from NumPy, and one using a Kaggle dataset about 2020-2021 Spotify songs.

# In[1]:


import altair as alt
import pandas as pd
import numpy as np
rng = np.random.default_rng()


# ## Basic example with random data

# In[2]:


# Making a 20x4 DataFrame filled with random integers.
A = rng.integers(0,100,size = (20,4))
rand_df = pd.DataFrame(A, columns = ["a","b","c","d"])


# In[3]:


rand_df


# In[4]:


alt.Chart(rand_df).mark_circle().encode(
    x = "a",
    y = "b"
)


# From the chart, it appears that there is only one point with `a` value less than 30.  Let's verify that in the dataset.

# In[5]:


(rand_df["a"] < 30).sum()


# In[6]:


rand_df[rand_df["a"] < 30]


# Here is another chart, where we color the points using column `c`, and we change the size of the points using column `d`.  We add a tooltip showing all the values, so put your mouse over a point to see its values of a,b,c,d.

# In[7]:


alt.Chart(rand_df).mark_circle().encode(
    x = "a",
    y = "b",
    color = "c",
    size = "d",
    tooltip = ["a","b","c","d"],
)


# ```{admonition} Exercise
# :class: tip
# Put your mouse over one of the points in the above chart.
# * How is the data reflected in the location, size, and color of the point?  
# * Can you find the row in `rand_df` corresponding to this point?
# * Choose another row in the DataFrame.  What point does it correspond to in the chart?
# ```

# ## Example with data from Spotify
# Download the `spotify_dataset.csv` file from Canvas, and put it somewhere you can access from Jupyter (maybe in the same folder as this notebook).
# 
# The dataset originally came from Kaggle [here](https://www.kaggle.com/sashankpillai/spotify-top-200-charts-20202021).  You can go there to see a description of the columns.

# In[8]:


# Change the path if necessary
# Doing some small "data cleaning": converting some columns from strings to numbers.
df = pd.read_csv("data/spotify_dataset.csv")
df = df.replace(" ",np.nan)
df["Streams"] = df["Streams"].str.replace(",","")
df.iloc[:,[5,7]] = df.iloc[:,[5,7]].apply(pd.to_numeric,axis=0).copy()
df.iloc[:,12:22] = df.iloc[:,12:22].apply(pd.to_numeric,axis=0).copy()


# In[9]:


df.dtypes


# In[10]:


brush = alt.selection_interval(empty='none')

chart = alt.Chart(df).mark_circle().encode(
    x = "Energy",
    y = "Loudness",
    color = alt.condition(brush,
                          alt.Color('Acousticness:Q', scale=alt.Scale(scheme='turbo',reverse=True)),
                          alt.value("lightgrey")),
).add_selection(
    brush,
).properties(
    width = 720,
    height = 450,
    title="Spotify dataset from Kaggle"
)

chart


# In[11]:


top_artists = df.Artist.value_counts()[:20].index.sort_values()


# In[12]:


df_top = df[df.Artist.isin(top_artists)]


# In[13]:


alt.Chart(df_top).mark_bar().encode(
    x = "Artist",
    y = "count()",
    color = "mean(Streams)"
)


# In[14]:


df.columns


# In[15]:


chart = alt.Chart(df).mark_circle().encode(
    x = "Energy",
    y = "Loudness",
    color = alt.Color('Acousticness:Q', scale=alt.Scale(scheme='turbo',reverse=True)),
    tooltip = ["Artist","Song Name","Release Date","Chord"]
).properties(
    width = 720,
    height = 450,
    title="Spotify dataset from Kaggle"
)

chart


# In[16]:


df[df["Loudness"] < -20]


# In[17]:


df.sort_values("Loudness", ascending=False)


# In[ ]:




