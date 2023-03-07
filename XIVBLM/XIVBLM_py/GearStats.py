import pandas as pd
from XIVBLM_py.GearSetFrameGen import GearSetFrameGen
def GearStats(MateriaFrame, GearSet):
    GearSetFrame = GearSetFrameGen(MateriaFrame, GearSet)[['WD', 'Int', 'DH', 'Crit', 'Det', 'SS']]
    GearSetFrame['WD'] = pd.to_numeric(GearSetFrame['WD'])
    GearSetFrame['Int'] = pd.to_numeric(GearSetFrame['Int'])
    GearSetFrame['DH'] = pd.to_numeric(GearSetFrame['DH'])
    GearSetFrame['Crit'] = pd.to_numeric(GearSetFrame['Crit'])
    GearSetFrame['Det'] = pd.to_numeric(GearSetFrame['Det'])
    GearSetFrame['SS'] = pd.to_numeric(GearSetFrame['SS'])
    return GearSetFrame.sum()
