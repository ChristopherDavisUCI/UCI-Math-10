# Monday Worksheet

On Friday, we ran K-Means clustering on the numeric columns from the Spotify dataset.  We should add an additional step, because it turns out that in the version from Friday, one of the dimensions ("input variables"/"features"/predictors") was dominating all the others.

## Warm-up with `any` and `all`

On Friday, we removed the rows which were bad in the Energy column, and were lucky that was good enough.  We really should have removed the rows that were bad in any column.  We can do that using either `any` or `all`.

* Using `rng.choice` and `pd.DataFrame`, make a 15x3 pandas DataFrame consisting of randomly chosen values of True and False.  Call it `df_bool`.
* Try evaluating `df_bool.any(axis = 1)`, `df_bool.all(axis = 1)`, `df_bool.any(axis = 0)`, `df_bool.all(axis = 0)` to learn about these `any` and `all` methods.

(This same syntax works for a NumPy array.  We asked you to convert it to a pandas DataFrame so that the values were easier to display in the notebook.)

## Identifying the problem

In a Jupyter notebook, we will basically follow [the procedure from Friday's class](Week6-Friday.ipynb), but a few changes.

* Import the Spotify dataset as `df` (be sure to use the `na_values` argument, so that the appropriate columns become numeric automatically).

* Verify that the correct columns are numeric, by using `dtypes`.

* Let's say a row is *bad* if any of its entries is NaN.  Using either `isna` or `notna` and either `any` or `all`, remove the bad rows from the DataFrame.  Call the result `df2`.  Put a `.copy()` afterwards just to be safe.

* Check your answer by computing the `shape` of `df2`.  It should be `(1545, 23)`.

* Get a list `numeric_cols` containing the names of all the numeric columns from `df2`.  Like on Friday, use `is_numeric_dtype`.  Your list should have length 14

* Make a new DataFrame `df3` containing only the numeric columns of `df2`.

* Instantiate a `KMeans` object, specifying 10 clusters.  Call the result `kmeans`.

* `fit` the object using `df3`.

* We are going to store the `cluster` values into the previous DataFrame `df2`, not in `df3`.  The reason that is better, is because `df2` contains information like artist name and song title.  Use code that's in the following form.

```
df2[???] = kmeans.predict(df2[???])
```

* Plot the result using the following code with Altair.  Make the colors look better by specifying the appropriate [encoding type](https://altair-viz.github.io/user_guide/encoding.html#encoding-data-types) for the color column.

```
alt.Chart(df2).mark_circle().encode(
    x = "Artist Followers",
    y = "Valence",
    color = "cluster"
)
```

* Our clusters are fit using 14-dimensional data, but one of those dimensions is dominating because the values in it are so much larger than the others.

* Check the mean and standard deviation of all the different columns in `df3` by using `df3.mean(axis = ???)` and `df3.std(axis = ???)`. (If you want to get numbers that are easier to read, without the scientific notation, you can change the way pandas displays float values, as in this [Stack Overflow answer](https://stackoverflow.com/a/21140339).)

## Fixing the problem using `StandardScaler`

This is such a common issue in Machine Learning (not just for clustering), that there is a built-in tool in scikit-learn to rescale the different columns.  The tool is called `StandardScaler`, and its syntax is very similar to the usual scikit-learn syntax.

* Import `StandardScaler` using the following code.

```
from sklearn.preprocessing import StandardScaler
```

* Instantiate a new `StandardScaler` object, and name it `scaler`.  Do this the same way you instantiate a `LinearRegression` object or a `KMeans` object.  You don't need to pass any arguments inside the parentheses.

* `fit` the object using `scaler.fit(df3)`.

* Normally we would try `scaler.predict(df3)`, but since we are not predicting anything, a different word is used.  Evaluate `scaler.transform(df3)`.  Convert it to a pandas DataFrame and name the result `df4`.  Give `df4` the same column names as `df3`.

You should think of `df4` and `df3` as containing the same data, with the only difference being that the data in `df4` has been normalized.

* Evaluate the mean and standard deviation of the columns of `df4`.

* Instantiate a new `KMeans` object with however many clusters you want.  `fit` the new object using `df4`, and then `predict` also using `df4`.  (It would be a little more robust to instead predict using `df2`, but then we would need another round of scaling and putting in column names.)  Put the resulting cluster numbers into the "cluster" column of `df2` (so overwrite the old "cluster" column.)

* Redo the Altair plot from above.  Add in a tooltip specifying the song name and artist name.  If everything went correctly, the colors should look less strictly ordered than before the scaling was done.
