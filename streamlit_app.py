## Please visit the online version in https://bmpmaster.streamlit.app

import streamlit as st
import pandas as pd
import os

st.write("""
# Biological and Medical Paper Master (BMPM)
*BMPM* is a LLM-driven reference paper reader. It applies the retrieval-augument generation framework to study the custom-defined paper library. 
""")

datDir = "data"
df = pd.read_csv(datDir + os.sep + "my_data.csv")
st.line_chart(df)
