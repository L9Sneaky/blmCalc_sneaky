import pandas as pd
import numpy as np
def GearSetFrameGen(MateriaFrame, GearSet):
    if str(type(GearSet)) == "<class 'pandas.core.frame.DataFrame'>":
        GearSetFrame = GearSet
    else:
        GearSetFrame = MateriaFrame.iloc[list(GearSet.values()), :]
    BaseRow = pd.DataFrame({'Name': [np.nan], 'Slot': ['Base'], 'WD': [0], 'Int': [447], 'Crit': [400], 'DH': [400], 'Det': [390], 'SS': [400]})
    GearSetFrame = pd.concat([GearSetFrame, BaseRow], ignore_index=True)
    return GearSetFrame
