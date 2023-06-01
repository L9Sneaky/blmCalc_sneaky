import pandas as pd
SlotsKeys = ["Weapon", "Head", "Chest", "Hands", "Legs", "Feet", "Ear", "Neck", "Wrist", "Finger1", "Finger2"]

def SortSet(GearSet):
    if type(GearSet) == dict:
        GearSet = {i: GearSet[i] for i in SlotsKeys}
    elif type(GearSet) == pd.core.frame.DataFrame:
        GearSet = GearSet.sort_index()
    return GearSet

def DftoSet(GearSet):
            
    return GearSet