import pandas as pd
SlotsKeys = ["Weapon", "Head", "Chest", "Hands", "Legs", "Feet", "Ear", "Neck", "Wrist", "Finger1", "Finger2"]

def SortSet(GearSet):
    if type(GearSet) == dict:
        GearSet = {i: GearSet[i] for i in SlotsKeys}
    elif type(GearSet) == pd.core.frame.DataFrame:
        GearSet = GearSet.sort_index()
    return GearSet

def DftoSet(GearSet):
    if type(GearSet) == pd.core.frame.DataFrame:
        dict = {key: None for key in SlotsKeys}
        for i in SlotsKeys:
            if i in ["Finger1" , "Finger2"] and ("Finger1" not in GearSet["Slot"].values or "Finger2" not in GearSet["Slot"].values):
                rings = list(GearSet[GearSet["Slot"] == "Finger"].index)
                dict["Finger1"] = rings[0]
                dict["Finger2"] = rings[1]
            else:
                dict[i] = list(GearSet[GearSet["Slot"] == i].index)[0]
    else:
        dict = GearSet
    return dict