## Please visit the online version in https://bmpmaster.streamlit.app

import streamlit as st
import pandas as pd
import numpy as np
import time
import os

st.write("""
# Biological and Medical Paper Master (BMPM)
*BMPM* is a LLM-driven reference paper reader. It applies the retrieval-augument generation framework to study the custom-defined paper library. 
""")

st.write("""
# Demo for Aneurysm studies
""")
datDir = "data"
df = pd.read_csv(datDir + os.sep + "my_data.csv")
st.line_chart(df)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()
# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")

