#!/usr/bin/env python
# coding: utf-8

# # Interactive
# * applymap/apply/map
# * value_counts
# * list comprehension hconcat

# In[1]:


import pandas as pd
import altair as alt
import numpy as np


# ## Example with data from Spotify
# Here we use the `spotify_dataset.csv` file from Canvas. The dataset originally came from Kaggle [here](https://www.kaggle.com/sashankpillai/spotify-top-200-charts-20202021).  The Kaggle page includes a description of the columns.
# 
# We perform some "cleaning" of the dataset.  By the end of Math 10, all of the following cell should be understandable, but for now, you shouldn't worry about the details of this "cleaning".
# 
# **Important**: You may need to change the path from `data/spotify_dataset.csv`, depending on where you have this csv file stored.

# In[2]:


df = pd.read_csv("data/spotify_dataset.csv") # change path if necessary
df = df.replace(" ",np.nan)
df["Streams"] = df["Streams"].str.replace(",","")
df.iloc[:,[5,7]] = df.iloc[:,[5,7]].apply(pd.to_numeric,axis=0).copy()
df.iloc[:,12:22] = df.iloc[:,12:22].apply(pd.to_numeric,axis=0).copy()


# ### Scatter plot

# The following Altair chart is just like what we made above with our random DataFrame.  We again use the column names to specify which parts of the data to use.  Before we used column names like "a" and "b".  Here the column names are more descriptive, like "Energy" and "Loudness".

# In[3]:


df = df[df["Chord"].notna()].copy()


# In[4]:


chords = sorted(list(set(df["Chord"])))


# In[5]:


chords


# In[6]:


df["Chord"].value_counts().max()


# In[7]:


df["Natural"] = df["Chord"].map(lambda x: 1 if len(x) == 1 else 0)


# In[8]:


brush = alt.selection_interval(empty='none')

chart1 = alt.Chart(df).mark_circle().encode(
    x = "Energy",
    y = "Valence",
    color = 'Chord',
    tooltip = ["Artist","Song Name","Release Date","Chord"]
).add_selection(
    brush,
)

chart2 = alt.Chart(df).mark_bar().encode(
    x = alt.X("Chord",scale=alt.Scale(domain=chords)),
    y = alt.Y("count()",scale=alt.Scale(domain=[0,220])),
    color="Chord",
).transform_filter(
    brush,
)

chart1 | chart2


# In[9]:


brush = alt.selection_single(empty='none',fields=["Chord"],on='mouseover')

chart1 = alt.Chart(df).mark_circle().encode(
    x = alt.X("Energy",scale=alt.Scale(domain=[0,1])),
    y = alt.Y("Valence",scale=alt.Scale(domain=[0,1])),
    color = 'Chord',
    tooltip = ["Artist","Song Name","Release Date","Chord"]
).transform_filter(
    brush
)

chart2 = alt.Chart(df).mark_bar().encode(
    x = alt.X("Chord",scale=alt.Scale(domain=chords)),
    y = alt.Y("count()",scale=alt.Scale(domain=[0,220])),
    color="Chord",
).add_selection(
    brush,
)

chart1 | chart2


# In[10]:


brush = alt.selection_multi(empty='none',fields=["Chord"],on='click')

chart1 = alt.Chart(df).mark_circle().encode(
    x = alt.X("Energy",scale=alt.Scale(domain=[0,1])),
    y = alt.Y("Valence",scale=alt.Scale(domain=[0,1])),
    color = 'Chord',
    tooltip = ["Artist","Song Name","Release Date","Chord"]
).transform_filter(
    brush
)

chart2 = alt.Chart(df).mark_bar().encode(
    x = alt.X("Chord",scale=alt.Scale(domain=chords)),
    y = alt.Y("count()",scale=alt.Scale(domain=[0,220])),
    color="Chord",
).add_selection(
    brush,
)

chart1 | chart2


# One of my favorite customizations in Altair is to use a more interesting color scheme.  Here is an example using the color scheme "goldred".  You can find more color options in the [Vega documentation](https://vega.github.io/vega/docs/schemes/).

# In[11]:


alt.Chart(df).mark_circle().encode(
    x = "Energy",
    y = "Loudness",
    color = alt.Color('Acousticness',scale=alt.Scale(scheme="goldred")),
    tooltip = ["Artist","Song Name","Release Date","Chord"]
)


# Sometimes the colors look more natural if they are reversed.  We do that by adding `reverse=True` in the `alt.Scale` component.

# In[12]:


alt.Chart(df).mark_circle().encode(
    x = "Energy",
    y = "Loudness",
    color = alt.Color('Acousticness',scale=alt.Scale(scheme="goldred",reverse=True)),
    tooltip = ["Artist","Song Name","Release Date","Chord"]
)


# (log-curve)=
# #### Spotify chart with tooltip
# 
# In the following chart we use a different color scheme, we specify the dimensions of the chart to make it a little bigger, and we give the chart a title.

# In[13]:


alt.Chart(df).mark_circle().encode(
    x = "Energy",
    y = "Loudness",
    color = alt.Color('Acousticness', scale=alt.Scale(scheme='turbo',reverse=True)),
    tooltip = ["Artist","Song Name","Release Date","Chord"]
).properties(
    width = 720,
    height = 450,
    title="Spotify dataset from Kaggle"
)


# ```{admonition} Caution
# :class: warning
# The rest of this notebook can be skipped on a first reading.  We give some more advanced examples.
# ```

# ### Histogram
# Here is an example of how to make a histogram using Altair.  The heights of the bars indicate how many total entries there are in that category.  The `count()` entry is not the name of a column.  Instead it is a special Altair function to count how often that entry occurs.

# In[14]:


alt.Chart(df).mark_bar().encode(
    x = "Artist",
    y = "count()"
)


# There are so many artists, this chart is pretty difficult to interpret.  Let's restrict ourselves to the top artists.
# 
# Here are the top 19 artists.  (Why 19 rather than 20?  No great reason, but this particular chart looks better with 19.)

# In[15]:


top_artists = df.Artist.value_counts()[:19]
top_artists


# Let's make our Altair chart using the sub-DataFrame with just these 19 top artists.  We make this using a new pandas method, `isin`.

# In[16]:


df_top = df[df.Artist.isin(top_artists.index)]
df_top.head()


# In[17]:


alt.Chart(df_top).mark_bar().encode(
    x = "Artist",
    y = "count()"
)


# Let's add color to the chart, using the average number of Streams for each artist.  In this example, `mean` is a special function in Altair, just like `count`.

# (spotify-bar)=
# #### Spotify bar chart

# In[18]:


alt.Chart(df_top).mark_bar().encode(
    x = "Artist",
    y = "count()",
    color = "mean(Streams)"
)


# ```{admonition} Exercise
# :class: tip
# Copy the above histogram code, and replace `mean` with `sum`.  Suddenly the colors are less interesting.  Why do you think that is?
# ```

# (Spotify-interactive)=
# ### Interactive example
# We end with an example just for inspiration.  One of the distinguishing features of Altair is its support for interactivity.  If you click and drag on the below chart, the points in the region you select will gain color.

# In[19]:


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

