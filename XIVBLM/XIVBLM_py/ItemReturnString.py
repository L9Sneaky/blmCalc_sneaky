import numpy as np

def ItemReturnString(MateriaFrame, EquipmentIndex):
    return MateriaFrame['Name'][EquipmentIndex] + ' (' + MateriaFrame['Materia'][EquipmentIndex] + ')'
