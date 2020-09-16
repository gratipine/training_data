import streamlit as st
import pandas as pd
import numpy as np
import os
import data_prep as dp
import numpy as np


st.title("From A to B")
data = dp.read_data()

st.dataframe(data.head())
destinations = np.sort(data["description"].unique())
origins = np.sort(data["origin_station"].unique())

origin_station = st.selectbox("Origin station: ", origins)

destination_station = st.selectbox("Destination station: ", destinations)

ticket_types = np.sort(data["ticket_code"].unique())
ticket_type = st.selectbox("Ticket type: ", ticket_types)

price = data.loc[
    (data["origin_station"] == origin_station) &
    (data["description"] == destination_station), :]

# TODO: Need to have a look at the ticket types
st.dataframe(price)