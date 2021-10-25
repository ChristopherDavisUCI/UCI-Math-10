# (Optional) Share a Streamlit App

(This is optional for now, but will be required before the end of the quarter.)

## Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/5KdCyMlU0-8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Instructions

Instructions from Streamlit are [here](https://docs.streamlit.io/streamlit-cloud/community).

The basic procedure is:
* Create a new repository on GitHub by going to [https://github.com/new](https://github.com/new)
* Upload the `.py` file(s) for your app and your `requirements.txt` file (see the next point).
* Make a `requirements.txt` file specifying the version number for the libraries you import.  You can find version numbers using `conda list` from a terminal, or using syntax like `np.__version__` (there are four total underscores in that code, two underscores on each side of version).  Here is what my requirements.txt file looked like:
```
numpy==1.20.3
streamlit==1.0.0
```
* Visit [https://share.streamlit.io/](https://share.streamlit.io/) to tell Streamlit where to find the app.
* After a few minutes, the app should then be visible to anyone through a link like [this](https://share.streamlit.io/christopherdavisuci/test/main/sessionstate.py).