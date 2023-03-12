import numpy as np

def Gear_Illegal(MateriaFrame, Gearset):
    if str(type(Gearset)) == "<class 'dict'>":
        judge = MateriaFrame.loc[list(Gearset.values()), ['Name', 'Unique']]
    else:
        judge = MateriaFrame.loc[Gearset.index, ['Name', 'Unique']]
    jury = judge.duplicated()
    return any(judge[jury]['Unique'])
