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
        # print(slot)
        gear_set.append(items.index[np.argmin(np.abs(items['Weights'] - weight_max))])
        # print(gear_set[-1])
    
    gear_set = [int(x) for x in gear_set]
    a = slots.tolist()
    index_to_replace = a.index('Finger')
    a[index_to_replace] = 'Finger1'
    slots = np.array(a)
    gear_set = dict(zip(slots, gear_set))
    
    if materia_frame.loc[gear_set['Finger1'], 'Unique']:
        items = materia_frame[materia_frame['Slot'] == 'Finger']
        items = items[items['Name'] != materia_frame.loc[gear_set['Finger1'], 'Name']]
    
    items['Weights'] = (DHWeight*items['DH'] + CritWeight*items['Crit'] +
                        DetWeight*items['Det'] + SSWeight*items['SS'])
    weight_max = np.max(items['Weights'])
    gear_set['Finger2'] = int(items.index[np.argmin(np.abs(items['Weights'] - weight_max))])
    gear_set = {key: gear_set[key] for key in sorted(gear_set)}

    del items, CritWeight, DetWeight, DHWeight, slot, slots, SSWeight, weight_max
    return gear_set


