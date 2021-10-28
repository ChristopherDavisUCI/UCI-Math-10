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

# pd.datetime notebook

```{code-cell} ipython3
import pandas as pd
```

```{code-cell} ipython3
df = pd.read_csv('../data/spotify_dataset.csv', na_values = " ")
```

```{code-cell} ipython3
df["Release Date"]
```

```{code-cell} ipython3
pd.to_datetime(df["Release Date"])
```

```{code-cell} ipython3
df.dtypes
```

```{code-cell} ipython3
df["Release Date"] = pd.to_datetime(df["Release Date"])
```

```{code-cell} ipython3
df.dtypes
```

```{code-cell} ipython3
df.loc[3,"Release Date"].day_name()
```

```{code-cell} ipython3
df.loc[3,"Release Date"].month_name()
```

```{code-cell} ipython3
df["Release Date"].map(lambda d: d.day_name())
```

```{code-cell} ipython3
:tags: ["output_scroll"]
df[df["Release Date"].map(lambda d: d.day_name()) == "Tuesday"]
```

```{code-cell} ipython3
df[df["Release Date"].map(lambda d: d.day_name()) == "Tuesday"].shape
```

```{code-cell} ipython3

```
