import pandas as pd
import streamlit as st

@st.cache
def read_data(pattern="./../data/prepped_data.csv"):
    return pd.read_csv(pattern)

