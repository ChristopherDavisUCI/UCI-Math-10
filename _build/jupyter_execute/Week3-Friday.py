#!/usr/bin/env python
# coding: utf-8

# # Week 3 - Friday Lecture
# Import the Spotify dataset from Canvas->Files->Datasets.
# 
# We've worked a lot with this dataset, but so far we have used some unexplained commands to "clean" the dataset after importing.  Today we'll go through the process of cleaning the dataset in a more systematic way.

# In[1]:


import pandas as pd
import altair as alt
import numpy as np


# In[2]:


# change path so it works on your computer
df = pd.read_csv("data/spotify_dataset.csv") 


# ## Data cleaning
# We get strange results if we try to use the Spotify dataset without any cleaning.

# In[3]:


alt.Chart(df[:50]).mark_circle().encode(
    x = "Energy",
    y = "Loudness"
)


# In[4]:


df["Loudness"].sum()


# In[5]:


df.dtypes


# In[6]:


df["Loudness"][:10]


# In[7]:


pd.to_numeric(df["Energy"])


# In[8]:


df.loc[30:40,"Energy"]


# In[9]:


df.replace(" ",np.nan)


# In[10]:


pd.to_numeric(df["Energy"])


# In[11]:


df = df.replace(" ",np.nan)


# In[12]:


pd.to_numeric(df["Energy"])


# In[13]:


df["Energy"] = pd.to_numeric(df["Energy"])


# In[14]:


pd.to_numeric(df["Streams"])


# In[15]:


int("48,633,449")


# In[16]:


df["Streams"].replace(",","")


# In[17]:


"mathematics".replace("t","10")


# In[18]:


"48,633,449".replace(",","")


# In[19]:


# equivalent to df.replace(" ",np.nan)
df.applymap(lambda x: np.nan if x == " " else x)


# In[20]:


df["Streams"].map(lambda s: s.replace(",",""))


# In[21]:


df["Streams"] = df["Streams"].map(lambda s: s.replace(",",""))


# In[22]:


df.head()


# In[23]:


df.dtypes


# ## Handling errors
# Let's write a function which takes as input a number x, and as output returns 3/x.

# In[24]:


def f(x):
    return 3/x


# In[25]:


f(5)


# In[26]:


f(0)


# What if we want to avoid this sort of error?  (For example, maybe this is part of a much longer program, and we don't want the whole program to crash if this function gets a bad input.)

# In[27]:


def f(x):
    if x == 0:
        return np.nan
    else:
        return 3/x


# In[28]:


f(10)


# In[29]:


f(0)


# In[30]:


type(f(0))


# We fixed the 0 error, but we will never catch all possible errors this way.

# In[31]:


f("5")


# We want something like
# ```
# def f(x):
#     if 3/x does not cause an error:
#         return 3/x
#     else:
#         return np.nan
# ```
# As far as I know, that can't be accomplished using an `if` statement.  We instead need to use the commands `try` and `except`.

# In[32]:


def f(x):
    try:
        return 3/x
    except:
        return "It didn't work"


# In[33]:


f(5)


# In[34]:


f("math 10")


# In[35]:


def can_divide(x):
    try:
        3/x
        return True
    except:
        return False


# In[36]:


can_divide(5)


# In[37]:


can_divide(0)


# ## Making columns numeric

# In[38]:


df.dtypes


# In[39]:


pd.to_numeric(df["Speechiness"])


# In[40]:


pd.to_numeric(df["Release Date"])


# In[41]:


# c column name
def can_be_numeric(c):
    try:
        pd.to_numeric(df[c])
        return True
    except:
        return False


# In[42]:


can_be_numeric("Release Date")


# In[43]:


can_be_numeric("Speechiness")


# In[44]:


# all the columns that can be numeric
good_cols = [c for c in df.columns if can_be_numeric(c)]
good_cols


# In[45]:


df[good_cols] = df[good_cols].apply(pd.to_numeric, axis=0)


# In[46]:


df.dtypes


# In[47]:


alt.Chart(df).mark_circle().encode(
    x = "Energy",
    y = "Loudness"
)


# In[48]:


chartlist = [alt.Chart(df).mark_circle().encode(
    x = "Energy",
    y = c
) for c in good_cols]


# In[49]:


chartlist


# In[50]:


chartlist[5]


# In[51]:


alt.hconcat(chartlist[0],chartlist[1])


# In[52]:


alt.hconcat(chartlist)


# In[53]:


m = alt.hconcat(*chartlist)


# In[54]:


m

