import pandas as pd
from XIVBLM_py.GearframeGenerate import Gearframe_Generate
from XIVBLM_py.MateriaAddFrame import MateriaAddFrame


def MateriaFrameGenerate(GearSetFilePath):
    print('Warning: You should see this message exactly ONCE')
    GearFrame = Gearframe_Generate(GearSetFilePath)
    MateriaFrame = pd.DataFrame()

    for i in range(GearFrame.shape[0]):
        ItemToAdd = MateriaAddFrame(GearFrame.iloc[i, :])
        MateriaFrame = pd.concat([MateriaFrame, ItemToAdd])

    MateriaFrame['Prune'] = None
    for i in range(MateriaFrame.shape[0]):
        MateriaFrame.at[i, 'Prune'] = len(set(MateriaFrame.query(f'WD >= {MateriaFrame.at[i, "WD"]}').index) & \
                                          set(MateriaFrame.query(f'Int >= {MateriaFrame.at[i, "Int"]}').index) & \
                                          set(MateriaFrame.query(f'Crit >= {MateriaFrame.at[i, "Crit"]}').index) & \
                                          set(MateriaFrame.query(f'DH >= {MateriaFrame.at[i, "DH"]}').index) & \
                                          set(MateriaFrame.query(f'Det >= {MateriaFrame.at[i, "Det"]}').index) & \
                                          set(MateriaFrame.query(f'SS >= {MateriaFrame.at[i, "SS"]}').index) & \
                                          set(MateriaFrame.query(f'Slot == "{MateriaFrame.at[i, "Slot"]}"').index))

    MateriaFrame = MateriaFrame[MateriaFrame['Prune'] == 1]
    MateriaFrame.drop(columns=['Prune'], inplace=True)
    MateriaFrame.reset_index(drop=True, inplace=True)

    return MateriaFrame
