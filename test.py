import pandas as pd
import numpy as np
from math import floor
import yaml
# %%
stat = ['DH' , 'Crit' , 'Det', 'Sps']
stats  = ['Direct Hit Rate', 'Critical Hit','Determination', 'Spell Speed']
name = []
type = []
ilvl = []
wd = []
int = []
DH = []
Crit = []
Det = []
Sps = []
slots = []
maxstat = []
AM = []
df = pd.read_csv('new 1.txt', sep='\t')
df.head()
df['Primary Substat'].unique()
for i in range(len(df)):
    w = df.iloc[i]
    name.append(w['Name'])
    type.append('Weapon' if w['ItemUICategory'] == 'Two–handed Thaumaturge\'s Arm' else w['ItemUICategory'])
    ilvl.append(w['iLvl'])
    wd.append(w['WD'])
    int.append(w['Main Stat'])
    dh = 0
    crit = 0
    det = 0
    sps = 0
    b = w['P. Value']
    a = stats.index(w['Primary Substat'])
    if a == 0:
        dh = b
    elif a == 1:
        crit = b
    elif a == 2:
        det = b
    elif a == 3:
        sps = b

    b = w['S. Value']
    a = stats.index(w['Secondary Substat'])
    if a == 0:
        dh = b
    elif a == 1:
        crit = b
    elif a == 2:
        det = b
    elif a == 3:
        sps = b

    DH.append(dh)
    Crit.append(crit)
    Det.append(det)
    Sps.append(sps)
    slots.append(w['# Slots'])
    maxstat.append(w['P. Value'])
    AM.append(w['Overmeld'])

t =pd.DataFrame(np.array([name, type, ilvl, wd, int, DH, Crit, Det, Sps, slots, maxstat, AM]).transpose(),
                columns=['Name' ,'Type','ilvl' ,'WD' ,'Int' ,'DH' ,'Crit' ,'Det', 'Sps', 'Slots', 'MaxStat', 'AM'])
t = t.drop_duplicates()
t = t.sort_values(['Type','ilvl'], ascending=[True,False]).reset_index(drop=True)
t['Type'].unique()
# %%
gear = {}
for i in t['Type'].unique():
    gear[i] = t[t['Type'] == i].to_dict(orient='records')
gear
# %%
with open(r'Gear_6.2.yaml', 'w') as file:
    documents = yaml.dump(gear, file, sort_keys=False)






# %%
