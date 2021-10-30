'''
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from sklearn.linear_model import LinearRegression

rng = np.random.default_rng()

st.title("Over-fitting")

m = 50
x = 10*rng.random(size=50) - 5
c = [3.2,6.5,-1.4]

y_true = c[0] + c[1]*x + c[2]*x**2

y = y_true + rng.normal(loc = 0, scale = 30, size = m)

df = pd.DataFrame({"x":x,"y_true":y_true, "y": y})


chart_data = alt.Chart(df).mark_circle(clip = True).encode(
    x = "x",
    y = "y"
)

chart_true = alt.Chart(df).mark_line().encode(
    x = "x",
    y = "y_true",
    color = alt.value("black"),
)

for i in range(1,21):
    df["x"+str(i)] = df["x"]**i

def poly_reg(df, d):
    reg = LinearRegression()
    X = df[[f"x{i}" for i in range(1,d+1)]]
    reg.fit(X,df["y"])
    return reg

def make_chart(df,d):
    df2 = df.copy()
    reg = poly_reg(df,d)
    X = df[[f"x{i}" for i in range(1,d+1)]]
    df2["y_pred"] = reg.predict(X)
    chart = alt.Chart(df2).mark_line(clip = True).encode(
        x = "x1",
        y = alt.Y("y_pred", scale = alt.Scale(domain=(-100,100))),
        color = alt.value("red"),
    )
    return chart

st.altair_chart(make_chart(df,2)+chart_data+chart_true)
'''