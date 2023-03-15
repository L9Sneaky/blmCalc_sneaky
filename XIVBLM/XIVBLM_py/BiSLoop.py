import numpy as np
from XIVBLM_py.Gear_Replace import Gear_Replace, Gear_Replace_DPS
from XIVBLM_py.FoodApply import food_apply
import pandas as pd

def BiSLoop(MateriaFrame, Food, GearSet):
    MateriaFrame['DPS'] = pd.Series(dtype=float)
    Temp = 1
    GearDPS = 0
    n = 0
    conf = 50
    while(Temp > GearDPS):
        if n >= conf:
            print(f'n over {conf}')
            break
        GearDPS = float(food_apply(MateriaFrame, GearSet, Food)['DPS'])
        for i in range(len(MateriaFrame)):
            MateriaFrame.loc[i, 'DPS'] = Gear_Replace_DPS(MateriaFrame, Food, GearSet, i)
        Temp = max(MateriaFrame['DPS'])
        print(f'n:{n} - Temp: {Temp} - GearDPS: {GearDPS}')
        NewPiece = MateriaFrame.loc[MateriaFrame['DPS'] == Temp].sample(n=1).index[0]
        GearSet = Gear_Replace(MateriaFrame, Food, GearSet, NewPiece)
        n += 1
    return GearSet