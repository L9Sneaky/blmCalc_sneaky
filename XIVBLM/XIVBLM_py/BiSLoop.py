import numpy as np
from XIVBLM_py.Gear_Replace import Gear_Replace, Gear_Replace_DPS
from XIVBLM_py.FoodApply import food_apply
import pandas as pd

def BiSLoop(MateriaFrame, Food, GearSet):
    MateriaFrame['DPS'] = pd.Series(dtype=float)
    Temp = 1
    GearDPS = 0
    n = 0
    conf = 6
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
    return GearSet, n >= conf

# def BiSLoop(MateriaFrame,Food,GearSet):
#   MateriaFrame['DPS'] = np.nan
#   Temp = 1
#   GearDPS = 0
#   while Temp > GearDPS:
#     GearDPS = Food.Apply(MateriaFrame,GearSet,Food)['DPS']
#     for i in range(0,MateriaFrame.shape[0]):
#       MateriaFrame['DPS'][i] = Gear_Replace_DPS(MateriaFrame,Food,GearSet,i)
#     Temp = MateriaFrame['DPS'].max()
#     print(Temp)
#     NewPiece = MateriaFrame['DPS'][MateriaFrame['DPS'] == Temp]
#     NewPiece = NewPiece.iloc[np.random.randint(0,len(NewPiece),1)]
#     GearSet = Gear_Replace(MateriaFrame,Food,GearSet,NewPiece)
#   return GearSet