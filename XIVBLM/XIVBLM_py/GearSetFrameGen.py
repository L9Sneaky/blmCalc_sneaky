import pandas as pd
import numpy as np
def GearSetFrameGen(MateriaFrame, GearSet):
    GearSetFrame = MateriaFrame.iloc[GearSet, :]
    BaseRow = pd.DataFrame({'Name': [np.nan], 'Slot': ['Base'], 'WD': [np.nan], 'Int': [np.nan], 'VIT': [0], 'Crit': [447], 'DH': [400], 'Det': [400], 'SS': [390], 'Level': [400]})
    GearSetFrame = pd.concat([GearSetFrame, BaseRow], ignore_index=True)
    return GearSetFrame
