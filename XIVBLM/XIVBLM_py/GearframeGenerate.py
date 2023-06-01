import numpy as np
import pandas as pd

GearType = pd.read_csv('XIVBLM/Tables/GearType.csv')
SecondaryStatCapValues = pd.read_csv('XIVBLM/Tables/SecondaryStatCapValues.csv', index_col=0)
WDValues = pd.read_csv('XIVBLM/Tables/WDValues.csv', index_col=0)
MainStatValues = pd.read_csv('XIVBLM/Tables/MainStatValues.csv', index_col=0)
SecondaryMinorValues = pd.read_csv('XIVBLM/Tables/SecondaryMinorValues.csv', index_col=0)

def Gearframe_Generate(InputSet, MajorMateriaValue=36, MinorMateriaValue=12):
    InputTable = pd.read_csv(InputSet)
    InputTable['StatCap'] = 0
    InputTable['WD'] = 0
    InputTable['Int'] = 0
    InputTable['DH'] = 0
    InputTable['Crit'] = 0
    InputTable['Det'] = 0
    InputTable['SS'] = 0
    InputTable['MateriaId1'] = 0
    InputTable['MateriaId2'] = 0
    InputTable['MateriaId3'] = 0
    InputTable['MateriaId4'] = 0
    InputTable['MateriaId5'] = 0

    MateriaRows = np.where(['Materia' in col for col in InputTable.columns])[0]

    GearFrame = pd.DataFrame()
    Slots = ["Weapon", "Head", "Chest", "Hands", "Legs", "Feet", "Ear", "Neck", "Wrist", "Finger"]

    for Slot in Slots:
        StatType = GearType.loc[GearType['Slot'] == Slot, 'Type'].iloc[0]

        Insert = InputTable.loc[InputTable['Slot'] == Slot, :].copy()

        N = len(Insert)
        Insert['Idx'] = range(1, N+1)
        Insert = Insert.reset_index()

        for i in range(N):
            ilvl = Insert.loc[i, 'Ilvl']
            CapValue = SecondaryStatCapValues.loc[ilvl,StatType]
            Insert.loc[i, 'StatCap'] = CapValue
            Insert.loc[i, 'WD'] = WDValues.loc[ilvl,StatType]
            Insert.loc[i, 'Int'] = MainStatValues.loc[ilvl,StatType]
            Insert.loc[i, Insert.loc[i, 'Primary']] = CapValue
            if Insert.loc[i, 'Name'] == 'Amazing Manderville Rod':
                Insert.loc[i, Insert.loc[i, 'Secondary']] = CapValue
            else:
                Insert.loc[i, Insert.loc[i, 'Secondary']] = SecondaryMinorValues.loc[ilvl,StatType]

            if Insert.loc[i, 'Overmeld']:
                MajorMeldRows = MateriaRows[:Insert.loc[i, 'Meld Slots'] + 1]
                Insert.iloc[i, MajorMeldRows+1] = MajorMateriaValue
                Insert.iloc[i, MateriaRows[Insert.loc[i, 'Meld Slots'] + 1 :] + 1] = MinorMateriaValue
            else:
                MajorMeldRows = MateriaRows[:Insert.loc[i, 'Meld Slots']]
                Insert.iloc[i, MajorMeldRows+1] = MajorMateriaValue

        Insert = Insert[['Slot', 'Idx', 'Ilvl', 'StatCap', 'Name', 'Unique', 'WD', 'Int', 'DH', 'Crit', 'Det', 'SS',
                         'MateriaId1', 'MateriaId2', 'MateriaId3', 'MateriaId4', 'MateriaId5']]
        GearFrame = pd.concat([GearFrame, Insert], ignore_index=True)

    GearFrame.index = range(1, len(GearFrame)+1)
    return GearFrame
