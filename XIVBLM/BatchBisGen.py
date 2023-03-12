import pandas as pd
from XIVBLM_py.MateriaFrameGenerate import MateriaFrameGenerate
from XIVBLM_py.StatWeightGearGen import StatWeightGearSet
from XIVBLM_py.BiSLoop import BiSLoop
from XIVBLM_py.ItemReturnString import ItemReturnString
from XIVBLM_py.FoodFrame import FoodFrame
from XIVBLM_py.FoodApply import food_apply




GearFile = 'XIVBLM/Gear Tables/DSR_BIS.csv'
MateriaFrame = MateriaFrameGenerate(GearFile)
GearFile = GearFile.replace('.csv', '')

Menu = pd.read_csv('XIVBLM/Tables/Menu.csv')
Food = FoodFrame(Menu=Menu, minIlvl=max(Menu.Ilvl))

StatWeightChart = pd.read_csv('XIVBLM/Tables/StatWeightStart.csv')

for i in range(len(StatWeightChart)):
    Set = StatWeightGearSet(MateriaFrame,
                            DHWeight=StatWeightChart['InitialDHWeight'][i],
                            CritWeight=StatWeightChart['InitialCritWeight'][i],
                            DetWeight=StatWeightChart['InitialDetWeight'][i],
                            SSWeight=StatWeightChart['InitialSSWeight'][i])

    print(f"Running set {i+1}/{len(StatWeightChart)}: DH={StatWeightChart['InitialDHWeight'][i]}, Crit={StatWeightChart['InitialCritWeight'][i]}, Det={StatWeightChart['InitialDetWeight'][i]}, SS={StatWeightChart['InitialSSWeight'][i]}")
    MateriaFrame = MateriaFrame.reset_index(drop=True)
    Set = BiSLoop(MateriaFrame, Food, Set)

    for slot in range(4, 14):
        StatWeightChart.iloc[i, slot] = ItemReturnString(MateriaFrame, Set[StatWeightChart.keys()[slot]])

    Attributes = food_apply(MateriaFrame, Set, Food)
    for slot in range(15, 23):
        StatWeightChart.iloc[i, slot] = Attributes[StatWeightChart.keys()[slot]]

StatWeightChart = StatWeightChart.sort_values(by=['DPS'], ascending=False)

OutputName = f"GearSetOutcomes{GearFile}"
StatWeightChart.to_csv(f"{OutputName} (Debug).csv", index=False)
StatWeightChart[~StatWeightChart.iloc[:, 16:24].duplicated()].iloc[:, 4:24].to_csv(f"{OutputName}.csv", index=False)
