# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:37:08 2025

@author: vhulenda.sumbana
"""
# My plot of data
import pandas as pd
import plotly.express as px

import streamlit as st

st.title("Streamlit is amazing")
st.write("Hello, Streamlit!")

st.header("Number selection")

data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})

#Display the data in the Streamlit app
st.write(data)

#Create a Plotly figure
fig = px.line(data, x="x", y="y", title="Simple Plotly Example")

# Display the plot in teh Streamlit app
st.plotly_chart(fig)

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")