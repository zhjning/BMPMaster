import streamlit as st
import pandas as pd
import os

st.write("""
# My first app
Hello *world!*
""")

datDir = "data"
df = pd.read_csv(datDir + os.sep + "my_data.csv")
st.line_chart(df)
