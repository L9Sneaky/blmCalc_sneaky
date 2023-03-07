import numpy as np
import random

def StatWeightGearSet(materia_frame, DHWeight=random.random(), CritWeight=random.random(),
                         DetWeight=random.random(), SSWeight=random.random()):
  
    slots = np.unique(materia_frame['Slot'])
    gear_set = []
    
    for slot in slots:
        items = materia_frame[materia_frame['Slot'] == slot]
        items['Weights'] = (DHWeight*items['DH'] + CritWeight*items['Crit'] +
                            DetWeight*items['Det'] + SSWeight*items['SS'])
        weight_max = np.max(items['Weights'])
        gear_set.append(items.index[np.argmin(np.abs(items['Weights'] - weight_max))])
    
    gear_set = [int(x) for x in gear_set]
    slots = slots[0:len(slots)-1]
    slots = np.append(slots, 'Finger1')
    gear_set = dict(zip(slots, gear_set))
    
    if materia_frame.loc[gear_set['Finger1'], 'Unique']:
        items = items[items['Name'] != materia_frame.loc[gear_set['Finger1'], 'Name']]
    
    items['Weights'] = (DHWeight*items['DH'] + CritWeight*items['Crit'] +
                        DetWeight*items['Det'] + SSWeight*items['SS'])
    weight_max = np.max(items['Weights'])
    gear_set['Finger2'] = int(items.index[np.argmin(np.abs(items['Weights'] - weight_max))])
    
    del items, CritWeight, DetWeight, DHWeight, slot, slots, SSWeight, weight_max
    return list(gear_set.values())


