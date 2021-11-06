---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Video quiz

There is just one video quiz this week, but it is a little more difficult than usual; it is meant as practice for the midterm.

Here is the documentation for the pandas method `pd.to_datetime`.  Notice that one of the allowable inputs is a pandas Series.

<iframe
  src="https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas-to-datetime"
  style="width:100%; height:300px;"
></iframe>

Here we try the `pd.to_datetime` function using a list as our input instead of a Series.

```{code-cell}
import pandas as pd

x = pd.to_datetime(["9/30/2021","10/7/2021","10/14/2021","10/21/2021"])
x
```

```{code-cell}
len(x)
```

```{code-cell}
type(x[0])
```

```{code-cell}
x[0].day_name()
```

```{code-cell}
x[1].month_name()
```

```{admonition} Practice Exercise
:class: hint

1. Import our usual Spotify dataset using the option `na_values=" "` to tell `pd.read_csv` that the blank spaces represent NaN values.
1. Convert the "Release Date" column so that it has datetime as its data type.
1. How many songs in our dataset were released on a Tuesday?
 ```


```{admonition} Video solution
:class: info

<iframe width="560" height="315" src="https://www.youtube.com/embed/QjfDg1s61SY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[Notebook from the video](datetime-notebook.ipynb)

 ```

```{admonition} Canvas video quiz
:class: attention

[Link to the Canvas quiz](https://canvas.eee.uci.edu/courses/39211/quizzes/194805)<br><br>Due Monday before lecture.
 ```


