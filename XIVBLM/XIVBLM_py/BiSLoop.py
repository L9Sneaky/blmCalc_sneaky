import numpy as np
from XIVBLM_py.Gear_Replace import Gear_Replace, Gear_Replace_DPS
from XIVBLM_py.FoodApply import food_apply

def BiSLoop(MateriaFrame, Food, GearSet):
    MateriaFrame['DPS'] = np.nan
    Temp = 1
    GearDPS = 0
    
    while Temp > GearDPS:
        GearDPS = float(food_apply(MateriaFrame, GearSet, Food)['DPS'])
        for i in range(MateriaFrame.shape[0]):
            MateriaFrame['DPS'][i] = Gear_Replace_DPS(MateriaFrame, Food, GearSet, i)
        Temp = np.nanmax(MateriaFrame['DPS'])
        print(Temp)
        
        NewPiece = np.where(MateriaFrame['DPS'] == Temp)[0]
        NewPiece = np.random.choice(NewPiece, size=1, replace=False)
        GearSet = Gear_Replace(MateriaFrame, Food, GearSet, NewPiece)
    
    return GearSet
