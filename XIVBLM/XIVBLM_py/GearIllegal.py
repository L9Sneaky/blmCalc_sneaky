import numpy as np

def Gear_Illegal(MateriaFrame, Gearset):
    judge = MateriaFrame.loc[Gearset, ['Name', 'Unique']]
    jury = judge.duplicated()
    return any(judge[jury]['Unique'])
