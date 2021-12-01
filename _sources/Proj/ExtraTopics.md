# Possible extra topics

One of the rubric items for the course project is to include something "extra" that wasn't covered in Math 10.  Here are a few possibilities.  It's even better if you find your own extra topic; it can be anything in Python that interests you.

## pandas styler

![pandas styler](../images/styler.png)

See these examples in the [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html#Styler-Functions).  This provides a way to highlight certain cells in a pandas DataFrame, and is good practice using `apply` and `applymap`.

## Altair interaction

![interactive gif](../images/altair.gif)

See [this section](Spotify-interactive) from these notes, or the [Altair documentation](https://altair-viz.github.io/user_guide/interactions.html).

## scikit-learn

[train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html). Next time I teach Math 10, I will be sure to introduce `train_test_split` early on when we discuss machine learning.

[Random forests](https://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees). This is maybe the machine learning method I see most often in Kaggle competitions.

![faces with pca](../images/pca.png)

[Principal component analysis](https://scikit-learn.org/stable/modules/decomposition.html#pca).  We saw clustering as our only example of unsupervised learning.  Another type of unsupervised learning is *dimensionality reduction*.  PCA is a famous example.

## Streamlit layout options

![streamlit cheat sheet](../images/streamlit-cheatsheet.png)

If you want to add some variety to the layout of your Streamlit app, there are a few different options.

[Gradient descent app](https://share.streamlit.io/christopherdavisuci/streamlit_ed/main/grad_desc.py).  Here is an app I made for our class (but I never ended up using it).  The box on the left is called a `sidebar`.  Here is the code that made the sidebar:
```
with st.sidebar:
    st.write("Here you can adjust some parameters for the gradient descent algorithm.")

    learn = st.slider("What learning rate?",min_value=0.0,max_value=0.2,step=0.002, value = init_alpha,
                key="alpha", on_change = update, format="%.3f")

    batch = st.slider("What batch size?",min_value=1,max_value=pts,step=1, value = init_batch,
                key="batch", on_change = update)
```
If you really want, you can see the [full code](https://github.com/ChristopherDavisUCI/streamlit_ed/blob/main/grad_desc.py) for the app, but I didn't make an attempt to have the code readable.

[Blog post](https://blog.streamlit.io/introducing-new-layout-options-for-streamlit/) introducing some of the other options for changing the layout in Streamlit.  I really like `columns`.

[on_change/on_click](https://blog.streamlit.io/session-state-for-streamlit/#callback-functions-and-session-state-api).  In the code example above I used a keyword argument called `on_change`, which specifies a function to call.  This is another way to add interactivity to a Streamlit app.  It is a good concept to learn, because it is used in many different contexts related to websites.