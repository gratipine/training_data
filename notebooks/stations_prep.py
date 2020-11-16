#%% Libraries
import json 
import pandas as pd
import sys
sys.path.append("..")
import src.faremap_data_prep as fdp
#%% 
# Opening JSON file 
name = "910GABDARE"
f = open(f'../{name}.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
# %%
data.get("fromId")

# %% Check what stations faremap is using
# Opening JSON file 
f = open('../stations.json',) 
  
# returns JSON object as  
# a dictionary 
stations_json = json.load(f) 
stations = fdp.prep_stations(stations_json)
stations.to_csv("..\data\stations.csv")
# %%
stations[stations["station_id"] == name]
# %%
