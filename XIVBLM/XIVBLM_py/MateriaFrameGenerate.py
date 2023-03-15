import pandas as pd
from XIVBLM_py.GearframeGenerate import Gearframe_Generate
from XIVBLM_py.AddMateria import MateriaAddFrame
import numpy as np

def MateriaFrameGenerate(GearSetFilePath=None):
    print('Warning: You should see this message exactly ONCE')
    GearFrame = Gearframe_Generate(GearSetFilePath)
    MateriaFrame = pd.DataFrame()

    for i in range(len(GearFrame)):
        ItemToAdd = MateriaAddFrame(GearFrame.iloc[i,:].to_frame().T)
        MateriaFrame = pd.concat([MateriaFrame, ItemToAdd], ignore_index=True)

    MateriaFrame['Prune'] = np.nan

    for i in range(len(MateriaFrame)):
        MateriaFrame.loc[i, 'Prune'] = len(
            set(MateriaFrame.loc[MateriaFrame['WD']>=MateriaFrame.loc[i, 'WD'], ].index).intersection(
            set(MateriaFrame.loc[MateriaFrame['Int']>=MateriaFrame.loc[i, 'Int'], ].index)).intersection(
            set(MateriaFrame.loc[MateriaFrame['Crit']>=MateriaFrame.loc[i, 'Crit'], ].index)).intersection(
            set(MateriaFrame.loc[MateriaFrame['DH']>=MateriaFrame.loc[i, 'DH'], ].index)).intersection(
            set(MateriaFrame.loc[MateriaFrame['Det']>=MateriaFrame.loc[i, 'Det'], ].index)).intersection(
            set(MateriaFrame.loc[MateriaFrame['SS']>=MateriaFrame.loc[i, 'SS'], ].index)).intersection(
            set(MateriaFrame.loc[MateriaFrame['Slot']==MateriaFrame.loc[i, 'Slot'], ].index))
            )
    
    MateriaFrame = MateriaFrame[MateriaFrame['Prune']==1]
    MateriaFrame = MateriaFrame.drop('Prune', axis=1).reset_index(drop=True)
    MateriaFrame.index = range(1, len(MateriaFrame)+1)
    
    return MateriaFrame
