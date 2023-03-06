import numpy as np

def GearSetFrameGen(MateriaFrame, GearSet):
    GearSetFrame = MateriaFrame.iloc[GearSet, :].copy()
    BaseRow = np.array([np.nan, 'Base', np.nan, np.nan, 0, 447, 400, 400, 390, 400])
    GearSetFrame.loc[len(GearSetFrame)] = BaseRow
    GearSetFrame.index = np.arange(1, len(GearSetFrame)+1)
    return GearSetFrame
