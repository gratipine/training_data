import streamlit as st
import pandas as pd
import numpy as np
import os
import data_prep as dp
import numpy as np


st.title("From A to B")
data = dp.read_data()

destinations = data["description"].unique()
destinations = destinations[~pd.isna(destinations)]
destinations = np.sort(destinations)

origins = data["origin_station"].unique()
origins = destinations[~pd.isna(destinations)]
origins = np.sort(destinations)

origin_station = st.sidebar.selectbox("Origin station: ", origins)

destination_station = st.sidebar.selectbox("Destination station: ", destinations)

price = data.loc[
    #(data["origin_station"] == origin_station) &
    #(data["description_ticket"] == ticket_type_required) &
    (data["description"] == destination_station), :] 

st.dataframe(price["origin_station"].unique())

ticket_types = list(price["description_ticket"].unique())

ticket_type_required = st.sidebar.selectbox("Ticket type: ", ticket_types, 0)

price = price[(price["description_ticket"] == ticket_type_required)]

st.dataframe(price)

st.dataframe(data[data["description"] == "HASLEMERE"])