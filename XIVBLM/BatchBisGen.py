import pandas as pd
import numpy as np
import random
pd.options.mode.chained_assignment = None  # default='warn'
from XIVBLM_py.MateriaFrameGenerate import MateriaFrameGenerate
from XIVBLM_py.StatWeightGearGen import StatWeightGearSet
from XIVBLM_py.BiSLoop import BiSLoop
from XIVBLM_py.ItemReturnString import ItemReturnString
from XIVBLM_py.FoodFrame import FoodFrame
from XIVBLM_py.FoodApply import food_apply
from XIVBLM_py.SortSet import SortSet
from XIVBLM_py.SortSet import DftoSet


GearFile = 'XIVBLM/6.4/Gear 6.4.csv'
MateriaFrame = MateriaFrameGenerate(GearFile)
GearFile = GearFile.replace('.csv', '')

OutputName = f"{GearFile} GearSetOutcomes"
file_name = GearFile.split('/')[-1]

Menu = pd.read_csv('XIVBLM/Tables/Menu.csv')
Food = FoodFrame(Menu=Menu, minIlvl=max(Menu.Ilvl))


StatWeightChart = pd.read_csv('XIVBLM/Tables/StatWeightStart.csv')
StatWeightChart_new = pd.DataFrame(columns=StatWeightChart.columns)
StatWeightChart['Gain'] = 0
baseDPS = 12656.52
nSkipped = 0
runs = 1000000
MateriaFrame = MateriaFrame.reset_index(drop=True)

for i in range(runs):
    if i < len(StatWeightChart):
        DHWeight=StatWeightChart['InitialDHWeight'][i]
        CritWeight=StatWeightChart['InitialCritWeight'][i]
        DetWeight=StatWeightChart['InitialDetWeight'][i]
        SSWeight=StatWeightChart['InitialSSWeight'][i]
        Set, _, _, _, _ = StatWeightGearSet(MateriaFrame,
                            DHWeight=DHWeight,
                            CritWeight=CritWeight,
                            DetWeight=DetWeight,
                            SSWeight=SSWeight)
    else:
        # np.random.seed(random.randint(0, 100000))
        DHWeight = np.random.randint(-50, 250)
        CritWeight = np.random.randint(-50, 250)
        DetWeight = np.random.randint(-50, 250)
        SSWeight = np.random.randint(-50, 250)
        Set, _, _, _, _ = StatWeightGearSet(MateriaFrame,
                            DHWeight=DHWeight,
                            CritWeight=CritWeight,
                            DetWeight=DetWeight,
                            SSWeight=SSWeight)
    print(f"Running set {i+1}/{runs}: DH={DHWeight}, Crit={CritWeight}, Det={DetWeight}, SS={SSWeight}")
    Set = SortSet(Set)
    Set, skip = BiSLoop(MateriaFrame, Food, Set)
    if skip:
        nSkipped += 1
        continue
    Attributes = food_apply(MateriaFrame, Set, Food)
    Set = DftoSet(Set)
    ChartDict = {key: None for key in list(StatWeightChart.keys())}
    ChartDict['InitialDHWeight'] = DHWeight
    ChartDict['InitialCritWeight'] = CritWeight
    ChartDict['InitialDetWeight'] = DetWeight
    ChartDict['InitialSSWeight'] = SSWeight

    for slot in StatWeightChart.keys()[4:15]:
        ChartDict[slot] = ItemReturnString(MateriaFrame, Set[slot])

    for slot in StatWeightChart.keys()[15:23]:
        ChartDict[slot] = Attributes[slot]
    
    ChartDict['Gain'] = str(((Attributes['DPS']/baseDPS)-1)*100)[:5] + '%'

    StatWeightChart_new = StatWeightChart_new.append(ChartDict, ignore_index=True)
    StatWeightChart_new = StatWeightChart_new.drop_duplicates(subset=StatWeightChart_new.columns, keep='first')
    StatWeightChart_new = StatWeightChart_new.sort_values(by=['DPS'], ascending=False)
    StatWeightChart_new = StatWeightChart_new[StatWeightChart_new['Gain'] != 0]
    StatWeightChart_new.to_csv(f"{OutputName} (Debug).csv", index=False)
    StatWeightChart_new[~StatWeightChart_new.iloc[:, 16:24].duplicated()].iloc[:, 4:24].to_csv(f"{OutputName}.csv", index=False)
print(f"Skipped {nSkipped} sets")