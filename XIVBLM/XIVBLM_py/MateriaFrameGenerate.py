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

    MateriaFrame.drop_duplicates(inplace=True)
    MateriaFrame.reset_index(drop=True, inplace=True)

    MateriaFrame['Prune'] = None
    for j in range(MateriaFrame.shape[0]):
        row = MateriaFrame.iloc[j]
        wd_query = f"WD >= {row['WD']}"
        int_query = f"Int >= {row['Int']}"
        crit_query = f"Crit >= {row['Crit']}"
        dh_query = f"DH >= {row['DH']}"
        det_query = f"Det >= {row['Det']}"
        ss_query = f"SS >= {row['SS']}"
        slot_query = f'Slot == "{row["Slot"]}"'
        prune_query = f"{wd_query} and {int_query} and {crit_query} and {dh_query} and {det_query} and {ss_query} and {slot_query}"
        MateriaFrame.at[j, 'Prune'] = len(MateriaFrame.query(prune_query).index) == 1

    MateriaFrame = MateriaFrame[MateriaFrame['Prune'] == True]
    MateriaFrame.drop(columns=['Prune'], inplace=True)
    MateriaFrame.reset_index(drop=True, inplace=True)

    return MateriaFrame
