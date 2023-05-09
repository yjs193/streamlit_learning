import streamlit as st
import numpy as np
import pandas as pd
st.title("This is my first app")
st.write("hello")
st.write("Here's our first attempt at using data to create a table:")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.write(chart_data)

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [23.13, 113.27],
    columns=['lat', 'lon'])
st.map(map_data)