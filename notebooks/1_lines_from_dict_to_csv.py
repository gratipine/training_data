#%% Libraries
import json 
import pandas as pd
import sys
sys.path.append("..")
import src.faremap_data_prep as fdp
import src.data_prep as prep
from importlib import reload

# %% Read in lines information
with open(f"../transport_lines.json") as file:
    lines = json.load(file)

# %% Data prep of lines information
out = prep.get_stations_in_line(lines)


# %% Get data on station names
f = open('../stations.json',) 
stations_json = json.load(f) 
stations = fdp.prep_stations(stations_json)
stations.to_feather("..\data\stations")


# %% Join station names and lines info 
lines_with_stations_on_them = out.merge(
    stations, on="station_id", how="left"
)


# %% save the data in
lines_with_stations_on_them.to_feather("..\data\lines_with_stations_on_them")
# %%
