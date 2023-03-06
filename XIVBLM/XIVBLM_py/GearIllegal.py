import numpy as np

def Gear_Illegal(MateriaFrame, Gearset):
    Judge = MateriaFrame.loc[Gearset, ['Name', 'Unique']]
    Jury = np.where(Judge.duplicated())[0]
    return any(Judge.iloc[Jury, :]['Unique'])
