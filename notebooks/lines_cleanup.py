#%% Libraries
import os
import json 
import pandas as pd
import sys
sys.path.append("..")
import src.faremap_data_prep as fdp
#%%
with open(f"../transport_lines.json") as file:
    lines = json.load(file)
# %%
lines_dt = pd.DataFrame()
for company_line in lines:
    print(company_line.get("lineName"))
    for branch in company_line.get("branches"):
        temp = fdp.line_to_dt(branch)
        temp["line"] = company_line.get("lineName")
        lines_dt = pd.concat([temp, lines_dt])
# %%
lines_dt.reset_index(inplace=True, drop=True)
lines_dt.to_feather("../data/lines_with_stations_from_faremap")
# %%
