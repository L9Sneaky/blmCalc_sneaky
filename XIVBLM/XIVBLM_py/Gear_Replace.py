import numpy as np
import pandas as pd
from XIVBLM_py.FoodApply import food_apply
from XIVBLM_py.SortSet import SortSet

# def Gear_Replace(MateriaFrame, Food, GearSet, NewPiece):
#     Slot = MateriaFrame.loc[NewPiece, 'Slot']
#     if Slot == "Finger":
#         Set1 = GearSet.copy()
#         Set1['Finger1'] = NewPiece
#         Set1_DPS = np.float64(food_apply(MateriaFrame, Set1, Food)['DPS'])

#         Set2 = GearSet.copy()
#         Set2['Finger2'] = NewPiece
#         Set2_DPS = np.float64(food_apply(MateriaFrame, Set2, Food)['DPS'])

#         if Set1_DPS > Set2_DPS:
#             GearSet['Finger1'] = NewPiece
#         else:
#             GearSet['Finger2'] = NewPiece
#     else:
#         GearSet[Slot] = NewPiece

#     return GearSet

def Gear_Replace(MateriaFrame, Food, GearSet, NewPiece):
    NewPieceItem = MateriaFrame.loc[NewPiece].to_frame().T
    Slot = NewPieceItem['Slot'].to_numpy()[0]
    CurrentGearSet = MateriaFrame.iloc[list(GearSet.values()), :]
    if Slot == "Finger":
        Set1 = CurrentGearSet.copy()

        Set1 = Set1.drop(GearSet['Finger1'])
        NewPieceItem.loc[:,"Slot"] = 'Finger1'
        Set1 = Set1.append(NewPieceItem)
        Set1_DPS = np.float64(food_apply(MateriaFrame, Set1, Food)['DPS'])

        Set2 = CurrentGearSet.copy()
        Set2 = Set2.drop(GearSet['Finger2'])
        NewPieceItem.loc[:,"Slot"] = 'Finger2'
        Set2 = Set2.append(NewPieceItem)
        Set2_DPS = np.float64(food_apply(MateriaFrame, Set2, Food)['DPS'])

        if Set1_DPS > Set2_DPS:
            GearSet['Finger1'] = NewPiece
        else:
            GearSet['Finger2'] = NewPiece
    else:
        CurrentGearSet = CurrentGearSet[CurrentGearSet['Slot'] != Slot]
        CurrentGearSet = CurrentGearSet.append(NewPieceItem)

    return CurrentGearSet


def Gear_Replace_DPS(MateriaFrame, Food, GearSet, NewPiece):
    NewPieceItem = MateriaFrame.loc[NewPiece].to_frame().T
    Slot = NewPieceItem['Slot'].to_numpy()[0]
    CurrentGearSet = MateriaFrame.iloc[list(GearSet.values()), :]
    # CurrentGearSet = GearSet
    if Slot == "Finger":
        Set1 = CurrentGearSet.copy()

        Set1 = Set1.drop(GearSet['Finger1'])
        NewPieceItem.loc[:,"Slot"] = 'Finger1'
        Set1 = Set1.append(NewPieceItem)
        Set1_DPS = np.float64(food_apply(MateriaFrame, Set1, Food)['DPS'])

        Set2 = CurrentGearSet.copy()
        Set2 = Set2.drop(GearSet['Finger2'])
        NewPieceItem.loc[:,"Slot"] = 'Finger2'
        Set2 = Set2.append(NewPieceItem)
        Set2_DPS = np.float64(food_apply(MateriaFrame, Set2, Food)['DPS'])

        if Set1_DPS > Set2_DPS:
            CurrentGearSet['Finger1'] = NewPiece
        else:
            CurrentGearSet['Finger2'] = NewPiece
    else:
        CurrentGearSet = CurrentGearSet[CurrentGearSet['Slot'] != Slot]
        CurrentGearSet = CurrentGearSet.append(NewPieceItem)
    GearSet = SortSet(GearSet)
    return np.float64(food_apply(MateriaFrame, GearSet, Food)['DPS'])
