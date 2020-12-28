#%% Libraries
import json 
import pandas as pd
import sys
sys.path.append("..")
import src.faremap_data_prep as fdp
import src.data_prep as prep
from importlib import reload

# %%
with open(f"../transport_lines.json") as file:
    lines = json.load(file)
# %%
out = prep.get_line_edges(lines[1:2])
# %%
list(lines[1].items())[2]
#%%
lines[1]
#%%
type(lines)
# %%
reload(prep)
# %%
