import numpy as np

def Gear_Replace(MateriaFrame, Food, GearSet, NewPiece):
    Slot = MateriaFrame.loc[NewPiece, 'Slot']
    if Slot == "Finger":
        Set1 = GearSet.copy()
        Set1['Finger1'] = NewPiece
        Set1_DPS = np.float64(Food.Apply(MateriaFrame, Set1, Food)['DPS'])

        Set2 = GearSet.copy()
        Set2['Finger2'] = NewPiece
        Set2_DPS = np.float64(Food.Apply(MateriaFrame, Set2, Food)['DPS'])

        if Set1_DPS > Set2_DPS:
            GearSet['Finger1'] = NewPiece
        else:
            GearSet['Finger2'] = NewPiece
    else:
        GearSet[Slot] = NewPiece

    return GearSet


def Gear_Replace_DPS(MateriaFrame, Food, GearSet, NewPiece):
    Slot = MateriaFrame.loc[NewPiece, 'Slot']
    if Slot == "Finger":
        Set1 = GearSet.copy()
        Set1['Finger1'] = NewPiece
        Set1_DPS = np.float64(Food.Apply(MateriaFrame, Set1, Food)['DPS'])

        Set2 = GearSet.copy()
        Set2['Finger2'] = NewPiece
        Set2_DPS = np.float64(Food.Apply(MateriaFrame, Set2, Food)['DPS'])

        if Set1_DPS > Set2_DPS:
            GearSet['Finger1'] = NewPiece
        else:
            GearSet['Finger2'] = NewPiece
    else:
        GearSet[Slot] = NewPiece

    return np.float64(Food.Apply(MateriaFrame, GearSet, Food)['DPS'])
