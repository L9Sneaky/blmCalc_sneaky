import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
from XIVBLM_py.MateriaFrameGenerate import MateriaFrameGenerate
from XIVBLM_py.StatWeightGearGen import StatWeightGearSet
from XIVBLM_py.BiSLoop import BiSLoop
from XIVBLM_py.ItemReturnString import ItemReturnString
from XIVBLM_py.FoodFrame import FoodFrame
from XIVBLM_py.FoodApply import food_apply
from XIVBLM_py.SortSet import SortSet


GearFile = 'XIVBLM/6.4/Crafted Gear.csv'
MateriaFrame = MateriaFrameGenerate(GearFile)
GearFile = GearFile.replace('.csv', '')

Menu = pd.read_csv('XIVBLM/Tables/Menu.csv')
Food = FoodFrame(Menu=Menu, minIlvl=max(Menu.Ilvl))


StatWeightChart = pd.read_csv('XIVBLM/Tables/StatWeightStart.csv')
StatWeightChart['Gain'] = 0
baseDPS = 12958.95
nSkipped = 0
runs = len(StatWeightChart)
MateriaFrame = MateriaFrame.reset_index(drop=True)
for i in range(runs):
    Set = StatWeightGearSet(MateriaFrame,
                            DHWeight=StatWeightChart['InitialDHWeight'][i],
                            CritWeight=StatWeightChart['InitialCritWeight'][i],
                            DetWeight=StatWeightChart['InitialDetWeight'][i],
                            SSWeight=StatWeightChart['InitialSSWeight'][i])
    print(f"Running set {i+1}/{runs}: DH={StatWeightChart['InitialDHWeight'][i]}, Crit={StatWeightChart['InitialCritWeight'][i]}, Det={StatWeightChart['InitialDetWeight'][i]}, SS={StatWeightChart['InitialSSWeight'][i]}")
    Set = SortSet(Set)
    Set, skip = BiSLoop(MateriaFrame, Food, Set)
    if skip:
        StatWeightChart.iloc[i, 4:23] = 'Skipped'
        nSkipped += 1
        continue
    # print(MateriaFrame.iloc[list(Set.values())])
    for slot in range(4, 15):
        StatWeightChart.iloc[i, slot] = ItemReturnString(MateriaFrame, Set[StatWeightChart.keys()[slot]])

    Attributes = food_apply(MateriaFrame, Set, Food)
    for slot in range(15, 23):
        StatWeightChart.iloc[i, slot] = Attributes[StatWeightChart.keys()[slot]]
    
    StatWeightChart.loc[i, 'Gain'] = str(((Attributes['DPS']/baseDPS)-1)*100)[:5] + '%'

# StatWeightChart = StatWeightChart.sort_values(by=['Gain'], ascending=False)

OutputName = f"{GearFile} GearSetOutcomes"
file_name = GearFile.split('/')[-1]
StatWeightChart = StatWeightChart[StatWeightChart['Gain'] != 0]
StatWeightChart.to_csv(f"{OutputName} (Debug).csv", index=False)
StatWeightChart[~StatWeightChart.iloc[:, 16:24].duplicated()].iloc[:, 4:24].to_csv(f"{OutputName}.csv", index=False)
print(f"Skipped {nSkipped} sets")