import numpy as np
import random

def StatWeightGearSet(materia_frame, DHWeight=np.random.uniform(-1, 1000000), CritWeight=np.random.uniform(-1, 1000000),
                         DetWeight=np.random.uniform(-1, 1000000), SSWeight=np.random.uniform(-1, 1000000)):
    
    if DetWeight == None or CritWeight == None or DHWeight == None or SSWeight == None:
        
        DHWeight = np.random.uniform(-1, 1000000)
        CritWeight = np.random.uniform(-1, 1000000)
        DetWeight = np.random.uniform(-1, 1000000)
        SSWeight = np.random.uniform(-1, 1000000)

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
    
    items = materia_frame[materia_frame['Slot'] == 'Finger']
    if materia_frame.loc[gear_set['Finger1'], 'Unique']:
        items = items[items['Name'] != materia_frame.loc[gear_set['Finger1'], 'Name']]
    
    items['Weights'] = (DHWeight*items['DH'] + CritWeight*items['Crit'] +
                        DetWeight*items['Det'] + SSWeight*items['SS'])
    weight_max = np.max(items['Weights'])
    gear_set['Finger2'] = int(items.index[np.argmin(np.abs(items['Weights'] - weight_max))])
    gear_set = {key: gear_set[key] for key in sorted(gear_set)}

    # del items, CritWeight, DetWeight, DHWeight, slot, slots, SSWeight, weight_max
    return gear_set, DHWeight, CritWeight, DetWeight, SSWeight


