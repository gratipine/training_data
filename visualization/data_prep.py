import pandas as pd
import streamlit as st

@st.cache
def read_data(pattern="./../data/prepped_data"):
    return pd.read_feather(pattern)

