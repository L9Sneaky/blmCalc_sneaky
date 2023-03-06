import numpy as np

def StatWeightGearSet(MateriaFrame, DHWeight=np.random.rand(), CritWeight=np.random.rand(),
                      DetWeight=np.random.rand(), SSWeight=np.random.rand()):
    
    Slots = np.unique(MateriaFrame['Slot'])
    Set = np.array([], dtype=np.int64)
    for slot in Slots:
        Items = MateriaFrame[MateriaFrame['Slot'] == slot]
        Items['Weights'] = DHWeight*Items['DH'] + CritWeight*Items['Crit'] + DetWeight*Items['Det'] + SSWeight*Items['SS']
        Weight_Max = np.max(Items['Weights'])
        Set = np.append(Set, int(Items.loc[Items['Weights'] == Weight_Max].index[0]))

    Set = Set.astype(np.int64)
    Slots = Slots[0:-1]
    Slots = np.append(Slots, 'Finger1')
    Set = np.append(Set, 0)
    Set = Set.astype(np.int64)
    Names = dict(zip(MateriaFrame.index, MateriaFrame['Name']))
    Unique = dict(zip(MateriaFrame.index, MateriaFrame['Unique']))
    
    if Unique[Set[-1]]:
        Items = MateriaFrame.drop(index=Set[-1])
        Items['Weights'] = DHWeight*Items['DH'] + CritWeight*Items['Crit'] + DetWeight*Items['Det'] + SSWeight*Items['SS']
        Weight_Max = np.max(Items['Weights'])
        Set[-1] = int(Items.loc[Items['Weights'] == Weight_Max].index[0])

    Set[-1] = int(Set[-1])
    Set[-2] = int(Set[-2])
    Set = np.append(Set, int(Items.loc[Items['Weights'] == Weight_Max].index[0]))
    Names[''] = 'Base'
    Names[Set[-1]] = 'Base'
    Names[Set[-2]] = 'Base'
    GearSetFrame = MateriaFrame.loc[Set].rename(index=Names)
    return GearSetFrame
