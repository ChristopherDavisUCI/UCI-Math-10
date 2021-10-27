# Remembering values in Streamlit

## Using `session_state` to access the value of a widget

Consider the following Streamlit code:

```
import streamlit as st

st.title(s)

s = st.text_input("Choose title")
```

This code will not work, because the line `st.title(s)` uses the undefined variable `s`.

Here is an attempt to fix this:

```
import streamlit as st

try:
    st.title(s)
except:
    st.title("Your title goes here")    

s = st.text_input("Choose title")
```

This code works in the sense that it does not throw an error, but we will never reach the `try` portion of the try-except block.  The title will always stay fixed as the default value.  The reason is that the variable `s` does not get remembered as the code reruns (as described [here](Week4/reruns-Streamlit.md)).

One solution to this is to use `st.session_state`.  Notice how similar this is to the above code.

```
import streamlit as st

try:
    s = st.session_state["my_title"]
    st.title(s)
except:
    st.title("Your title goes here")

st.text_input("Choose title", key = "my_title")
```

By specifying the `key` for the text input widget, we can access the value of that widget using `st.session_state["my_title"]`.

Here is another way of doing the same thing, but where we replace the try-except block with an if statement.

## Using `session_state` to remember a value

As another example of using `session_state`, we have the following.

```
import streamlit as st
import numpy as np

rng = np.random.default_rng()

if "a" not in st.session_state:
    A = rng.random((1,5))
    st.session_state["a"] = A
else:
    A = st.session_state["a"]
    
st.write(A)

st.slider("A slider",0,100,40,1)
```
Ordinarily, [Streamlit reruns](Week4/reruns-Streamlit.md) would cause the array `A` to change every time the slider is moved, but by using `st.session_state`, we are able to remember the value of `A` from one execution of the code to the next.