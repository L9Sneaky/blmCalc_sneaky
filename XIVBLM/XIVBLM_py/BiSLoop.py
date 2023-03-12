import numpy as np
from XIVBLM_py.Gear_Replace import Gear_Replace, Gear_Replace_DPS
from XIVBLM_py.FoodApply import food_apply
import pandas as pd

def BiSLoop(MateriaFrame, Food, GearSet):
    MateriaFrame['DPS'] = pd.Series(dtype=float)
    Temp = 1
    GearDPS = 0
    n = 0
    while(Temp > GearDPS):
        if n >= 50:
            print('n over 50')
            break
        GearDPS = float(food_apply(MateriaFrame, GearSet, Food)['DPS'])
        for i in range(len(MateriaFrame)):
            MateriaFrame.loc[i, 'DPS'] = Gear_Replace_DPS(MateriaFrame, Food, GearSet, i)
        Temp = max(MateriaFrame['DPS'])
        print(Temp)
        NewPiece = MateriaFrame.loc[MateriaFrame['DPS'] == Temp].sample(n=1).index[0]
        GearSet = Gear_Replace(MateriaFrame, Food, GearSet, NewPiece)
        n += 1

    return GearSet