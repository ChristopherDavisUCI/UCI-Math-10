# Streamlit

We will use Streamlit to create shareable apps.

**Workflow for Streamlit**

Here is the basic process we will follow.

* Write a Python file, say `myapp.py`, like the following.
```
import streamlit as st

st.title("My first app")

s = st.slider("A slider widget", 0, 10, 4)

st.write(f"You have selected {s}")
```
* Execute the file from a terminal using the following command.
```
streamlit run myapp.py
```
* View the compiled app in a web browser (which should open automatically).  It will look something like the following.
![slider image](images/slider.png)
* To stop the server that makes the app visible in your browser, return to the terminal and hit Control+C.
* When we're finished modifying the app, we can put the code onto GitHub and share the app via Streamlit Cloud.

**Troubleshooting**

If the above process (everything before the GitHub step) does not work, there are two most likely issues.
* Do you have Streamlit installed?
* Are you executing `streamlit run myapp.py` from the correct folder?  You could try using a more precise description of the file location: `streamlit run /Users/christopherdavis/Desktop/Sample\ Folder/myapp.py`

**Where to edit `.py` files**

This is the first time we will work with `.py` files.  (In a more traditional Python course, you might spend 100% of your time working with these files, and never use Jupyter Notebook.)  These `.py` files should be edited in a text editor, rather than in Jupyter Notebook.

Probably the easiest place to edit a py file is Spyder from within Anaconda Navigator.  On my personal computer that didn't work well (it had slow typing, but it seems to work well on the lab computers), so I [downloaded Spyder](https://www.spyder-ide.org/#section-download) separately and used that.

Another (also free) option is to use Visual Studio Code which is also available in Anaconda Navigator.  [Visual Studio Code](https://code.visualstudio.com/) (outside of Anaconda Navigator) is what I personally use in real life (it's what I am using as I type this sentence), but I think Spyder works more easily "out of the box".

If you have experience with any other text editor for coding, you are very welcome to use that.  Here are some other choices (Links to an external site.) listed by the website Real Python.  That is a very good site, although the article might be a little old (about 5 years).

**Streamlit documentation**

You can read more about Streamlit in the [Streamlit documentation](https://docs.streamlit.io/).