import yaml
import pandas as pd
from main import getEveryMeld, getAllMeldOption
# %%
with open("Gear_6.2_preBis.yaml", 'r') as stream:
    gear = yaml.safe_load(stream)

gear1 = []
for i in gear.keys():
    gear1.append(gear[i][0])
    # print(gear[i][0])
df = pd.DataFrame(gear1)
