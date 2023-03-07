import pandas as pd
from XIVBLM_py.GearframeGenerate import Gearframe_Generate
from XIVBLM_py.AddMateria import MateriaAddFrame
import numpy as np

# def MateriaFrameGenerate(GearSetFilePath):
#     print('Warning: You should see this message exactly ONCE')
#     GearFrame = Gearframe_Generate(GearSetFilePath)
#     MateriaFrame = pd.DataFrame()

#     for i in range(GearFrame.shape[0]):
#         ItemToAdd = MateriaAddFrame(GearFrame.iloc[i, :])
#         MateriaFrame = pd.concat([MateriaFrame, ItemToAdd])

#     MateriaFrame.drop_duplicates(inplace=True)
#     MateriaFrame.reset_index(drop=True, inplace=True)

#     MateriaFrame['Prune'] = None
#     for j in range(MateriaFrame.shape[0]):
#         row = MateriaFrame.iloc[j]
#         wd_query = f"WD >= {row['WD']}"
#         int_query = f"Int >= {row['Int']}"
#         crit_query = f"Crit >= {row['Crit']}"
#         dh_query = f"DH >= {row['DH']}"
#         det_query = f"Det >= {row['Det']}"
#         ss_query = f"SS >= {row['SS']}"
#         slot_query = f'Slot == "{row["Slot"]}"'
#         prune_query = f"{wd_query} and {int_query} and {crit_query} and {dh_query} and {det_query} and {ss_query} and {slot_query}"
#         MateriaFrame.at[j, 'Prune'] = len(MateriaFrame.query(prune_query).index) == 1

#     MateriaFrame = MateriaFrame[MateriaFrame['Prune'] == True]
#     MateriaFrame.drop(columns=['Prune'], inplace=True)
#     MateriaFrame.reset_index(drop=True, inplace=True)

#     return MateriaFrame

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
