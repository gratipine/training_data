#%%
import json 
import pandas as pd
import sys
sys.path.append("..")
import src.faremap_data_prep as fdp
import src.data_prep as prep
from importlib import reload


#%% Read in data
lines_with_stations_on_them = pd.read_feather(
    "..\data\lines_with_stations_on_them")

# %%
from_station = ""
to_station = ""
# %%
len(lines_with_stations_on_them[
    pd.isna(lines_with_stations_on_them["station_name"])]) / len(lines_with_stations_on_them)
# %% drop the NAs for easier handling for now
lines_with_stations_on_them_complete = lines_with_stations_on_them[
    ~pd.isna(lines_with_stations_on_them["station_name"])]
# %%
# %%
from_station_lines = (
    lines_with_stations_on_them_complete.loc[
        (lines_with_stations_on_them_complete["station_name"] == from_station)]
        .drop_duplicates()) 

to_station_lines = (
    lines_with_stations_on_them_complete[
        (lines_with_stations_on_them_complete["station_name"] == to_station)]
    .drop_duplicates())


# %%
combined_lines = from_station_lines.merge(
    to_station_lines, on=["line_start", "line_end", "line_name"], 
    suffixes=["_from", "_to"], how="outer")
# %%
