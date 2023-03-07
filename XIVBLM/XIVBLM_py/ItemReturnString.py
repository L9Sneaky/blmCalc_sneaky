import numpy as np

def ItemReturnString(MateriaFrame, EquipmentIndex):
    mask = MateriaFrame['Name'].isin(EquipmentIndex['Name'])
    index = MateriaFrame.index[mask]
    return MateriaFrame['Name'][index] + ' (' + MateriaFrame['Materia'][index] + ')'
