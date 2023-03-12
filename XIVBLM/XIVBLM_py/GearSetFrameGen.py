import pandas as pd
import numpy as np
def GearSetFrameGen(MateriaFrame, GearSet):
    if str(type(GearSet)) == "<class 'pandas.core.frame.DataFrame'>":
        GearSetFrame = GearSet
    else:
        GearSetFrame = MateriaFrame.iloc[list(GearSet.values()), :]
    BaseRow = pd.DataFrame({'Name': [np.nan], 'Slot': ['Base'], 'WD': [np.nan], 'Int': [np.nan], 'VIT': [0], 'Crit': [447], 'DH': [400], 'Det': [400], 'SS': [390], 'Level': [400]})
    GearSetFrame = pd.concat([GearSetFrame, BaseRow], ignore_index=True)
    return GearSetFrame
