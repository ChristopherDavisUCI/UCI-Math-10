---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# First two examples of Altair Charts
We give two examples, one produced with random data from NumPy, and one using a Kaggle dataset about top 2020-2021 Spotify songs.

```{code-cell} ipython3
import altair as alt
import pandas as pd
import numpy as np
rng = np.random.default_rng()
```

## Basic example with random data
We first make a $20 \times 4$ NumPy array of random integers in NumPy, and then convert it to a pandas DataFrame.

```{code-cell} ipython3
A = rng.integers(0,100,size = (20,4))
rand_df = pd.DataFrame(A, columns = ["a","b","c","d"])
```

```{code-cell} ipython3
rand_df
```

Each row in the DataFrame will correspond to a point in our chart.  The values in the $a$ column and $b$ column correspond to the $x$-coordinate and the $y$-coordinate, respectively.

Here we use `mark_line` to connect the datapoints with lines.

The syntax for making an Altair chart can be intimidating.  The faster you can get comfortable with it, the better.

```{code-cell} ipython3
alt.Chart(rand_df).mark_line().encode(
    x = "a",
    y = "b"
)
```

The same data, but with disks drawn instead of lines: we changed from `mark_line` to `mark_circle`.

```{code-cell} ipython3
alt.Chart(rand_df).mark_circle().encode(
    x = "a",
    y = "b"
)
```

By looking at the chart, how many points have an `a` value less than 30?  Let's verify that in the dataset.

```{code-cell} ipython3
(rand_df["a"] < 30).sum()
```

Here are those points explicitly.

```{code-cell} ipython3
rand_df[rand_df["a"] < 30]
```

Here is another chart, where we color the points using column `c`, and we change the size of the points using column `d`.  We add a tooltip showing all the values, so put your mouse over a point to see its values of a,b,c,d.

```{code-cell} ipython3
alt.Chart(rand_df).mark_circle().encode(
    x = "a",
    y = "b",
    color = "c",
    size = "d",
    tooltip = ["a","b","c","d"],
)
```

```{admonition} Exercise
:class: tip
Put your mouse over one of the points in the above chart.
* How is the underlying data for that point reflected in its location, size, and color?  
* Can you find the row in `rand_df` corresponding to this point?
* Choose another row in the DataFrame.  What point does it correspond to in the chart?

For your convenience, the original pandas DataFrame is shown below.
```

```{code-cell} ipython3
rand_df
```

Another example with more points, and where we add an *opacity* channel.

```{code-cell} ipython3
A = rng.integers(0,100,size = (1000,5))
rand_df2 = pd.DataFrame(A, columns = ["a","b","c","d","e"])
```

```{code-cell} ipython3
alt.Chart(rand_df2).mark_circle().encode(
    x = "a",
    y = "b",
    color = "c",
    size = "d",
    opacity = "e",
    tooltip = ["a","b","c","d","e"],
)
```

```{admonition} Exercise
:class: tip
I don't like the `d` and `e` parts of the legend.  Can you figure out how to remove them, by mimicking an example from the [documentation](https://altair-viz.github.io/user_guide/customization.html?highlight=legend#adjusting-the-legend)?
```

+++

It's hard to recognize the opacity in the above example.  Let's change the DataFrame so that all the points to the left of $a = 40$ are only 15% transparent, and the rest of the points are 100% opaque.  We add a `scale=None` to the opacity channel so we have complete control over the opacity.

```{code-cell} ipython3
rand_df2["e"] = 1
rand_df2.loc[(rand_df2["a"] < 40),"e"] = 0.15
```

```{code-cell} ipython3
alt.Chart(rand_df2).mark_circle().encode(
    x = "a",
    y = "b",
    color = "c",
    size = "d",
    opacity = alt.Opacity("e",scale=None),
    tooltip = ["a","b","c","d","e"],
)
```

## Example with data from Spotify
Here we use the `spotify_dataset.csv` file from Canvas. The dataset originally came from Kaggle [here](https://www.kaggle.com/sashankpillai/spotify-top-200-charts-20202021).  The Kaggle page includes a description of the columns.

We perform some "cleaning" of the dataset.  By the end of Math 10, all of the following cell should be understandable, but for now, you shouldn't worry about the details of this "cleaning".

**Important**: You may need to change the path from `data/spotify_dataset.csv`, depending on where you have this csv file stored.

```{code-cell} ipython3
df = pd.read_csv("../data/spotify_dataset.csv") # change path if necessary
df = df.replace(" ",np.nan)
df["Streams"] = df["Streams"].str.replace(",","")
df.iloc[:,[5,7]] = df.iloc[:,[5,7]].apply(pd.to_numeric,axis=0).copy()
df.iloc[:,12:22] = df.iloc[:,12:22].apply(pd.to_numeric,axis=0).copy()
```

```{code-cell} ipython3
df.head()
```

If there are more than 5000 rows, then we need to do some data preprocessing before giving the DataFrame to Altair.  But in this case, there are only 1556 rows.

```{code-cell} ipython3
df.shape
```

If a column has type `object`, that often means it is a string, even if the values look numerical.  If you're having a hard time plotting data, make sure the values are numbers and not strings.  The main point of the data-cleaning we did above was to make more of the columns numerical.  Of course, a column like *Song Name* is never going to be numerical.

```{code-cell} ipython3
df.dtypes
```

### Scatter plot

+++

The following Altair chart is just like what we made above with our random DataFrame.  We again use the column names to specify which parts of the data to use.  Before we used column names like "a" and "b".  Here the column names are more descriptive, like "Energy" and "Loudness".

```{code-cell} ipython3
alt.Chart(df).mark_circle().encode(
    x = "Energy",
    y = "Loudness",
    color = 'Acousticness',
    tooltip = ["Artist","Song Name","Release Date","Chord"]
)
```

One of my favorite customizations in Altair is to use a more interesting color scheme.  Here is an example using the color scheme "goldred".  You can find more color options in the [Vega documentation](https://vega.github.io/vega/docs/schemes/).

```{code-cell} ipython3
alt.Chart(df).mark_circle().encode(
    x = "Energy",
    y = "Loudness",
    color = alt.Color('Acousticness',scale=alt.Scale(scheme="goldred")),
    tooltip = ["Artist","Song Name","Release Date","Chord"]
)
```

Sometimes the colors look more natural if they are reversed.  We do that by adding `reverse=True` in the `alt.Scale` component.

```{code-cell} ipython3
alt.Chart(df).mark_circle().encode(
    x = "Energy",
    y = "Loudness",
    color = alt.Color('Acousticness',scale=alt.Scale(scheme="goldred",reverse=True)),
    tooltip = ["Artist","Song Name","Release Date","Chord"]
)
```

(log-curve)=
#### Spotify chart with tooltip

In the following chart we use a different color scheme, we specify the dimensions of the chart to make it a little bigger, and we give the chart a title.

```{code-cell} ipython3
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
```

```{admonition} Caution
:class: warning
The rest of this notebook can be skipped on a first reading.  We give some more advanced examples.
```

+++

### Histogram
Here is an example of how to make a histogram using Altair.  The heights of the bars indicate how many total entries there are in that category.  The `count()` entry is not the name of a column.  Instead it is a special Altair function to count how often that entry occurs.

```{code-cell} ipython3
:tags: [output_scroll]
alt.Chart(df).mark_bar().encode(
    x = "Artist",
    y = "count()"
)
```

There are so many artists, this chart is pretty difficult to interpret.  Let's restrict ourselves to the top artists.

Here are the top 19 artists.  (Why 19 rather than 20?  No great reason, but this particular chart looks better with 19.)

```{code-cell} ipython3
top_artists = df.Artist.value_counts()[:19]
top_artists
```

Let's make our Altair chart using the sub-DataFrame with just these 19 top artists.  We make this using a new pandas method, `isin`.

```{code-cell} ipython3
df_top = df[df.Artist.isin(top_artists.index)]
df_top.head()
```

```{code-cell} ipython3
alt.Chart(df_top).mark_bar().encode(
    x = "Artist",
    y = "count()"
)
```

Let's add color to the chart, using the average number of Streams for each artist.  In this example, `mean` is a special function in Altair, just like `count`.

+++

(spotify-bar)=
#### Spotify bar chart

```{code-cell} ipython3
alt.Chart(df_top).mark_bar().encode(
    x = "Artist",
    y = "count()",
    color = "mean(Streams)"
)
```

```{admonition} Exercise
:class: tip
Copy the above histogram code, and replace `mean` with `sum`.  Suddenly the colors are less interesting.  Why do you think that is?
```

+++

(Spotify-interactive)=
### Interactive example
We end with an example just for inspiration.  One of the distinguishing features of Altair is its support for interactivity.  If you click and drag on the below chart, the points in the region you select will gain color.

```{code-cell} ipython3
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
```
