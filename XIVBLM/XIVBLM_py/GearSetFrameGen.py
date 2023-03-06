import numpy as np

def GearSetFrameGen(MateriaFrame, GearSet):
    GearSetFrame = MateriaFrame[GearSet, :]
    BaseRow = np.array([np.nan, 'Base', np.nan, np.nan, 0, 447, 400, 400, 390, 400])
    GearSetFrame = np.vstack((GearSetFrame, BaseRow))
    GearSetFrame = GearSetFrame.astype(np.float64)
    return GearSetFrame
