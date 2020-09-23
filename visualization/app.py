import streamlit as st
import pandas as pd
import numpy as np
import os
import data_prep as dp
import numpy as np


st.title("From A to B")
data = dp.read_data()


#st.dataframe(data[data["description_ticket"] == ticket_type_required].head())
destinations = np.sort(data["description"].unique())
origins = np.sort(data["origin_station"].unique())

origin_station = st.sidebar.selectbox("Origin station: ", origins)

destination_station = st.sidebar.selectbox("Destination station: ", destinations)

price = data.loc[
    #(data["origin_station"] == origin_station) &
    #(data["description_ticket"] == ticket_type_required) &
    (data["description"] == destination_station), :]

ticket_types = list(price["description_ticket"].unique())

ticket_type_required = st.sidebar.selectbox("Ticket type: ", ticket_types, 0)

price = price[(price["description_ticket"] == ticket_type_required)]

# TODO: Need to have a look at the ticket types
st.dataframe(price)

st.dataframe(data[data["description"] == "HASLEMERE"])