import streamlit as st
import pandas as pd

# from ucimlrepo import fetch_ucirepo
# https://archive.ics.uci.edu/dataset/352/online+retail

# read df from csv iris dataset from CSV files
df = pd.read_csv('data.csv', encoding="ISO-8859-1")

# hello world
st.title('Hello World!')
# Read the header of X
st.write("Header of X:")
st.write(df)

st.write('This is e-commerce RFM targets')
# st.dataframe(y)
