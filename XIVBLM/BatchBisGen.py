import pandas as pd
from XIVBLM_py.MateriaFrameGenerate import MateriaFrameGenerate
from XIVBLM_py.FoodFrame import FoodFrame
from XIVBLM_py.StatWeightGearGen import StatWeightGearSet
from XIVBLM_py.BiSLoop import BiSLoop
from XIVBLM_py.ItemReturnString import ItemReturnString

# Load gear file
GearFile = "/home/hp/personal/blmCalc_sneaky/XIVBLM/Gear Tables/DSR_BIS.csv"
MateriaFrame = MateriaFrameGenerate(GearFile)
GearFile = GearFile.replace('.csv', '')

# Load food data
Menu = pd.read_csv('Tables/Menu.csv')
Food = FoodFrame(Menu=Menu, minIlvl=max(Menu['Ilvl']))

# Load stat weights
StatWeightChart = pd.read_csv("Tables\\StatWeightStart.csv")

for i in range(len(StatWeightChart)):
    Set = StatWeightGearSet(MateriaFrame,
                            DHWeight=StatWeightChart['InitialDHWeight'][i],
                            CritWeight=StatWeightChart['InitialCritWeight'][i],
                            DetWeight=StatWeightChart['InitialDetWeight'][i],
                            SSWeight=StatWeightChart['InitialSSWeight'][i])

    print(f"Running set {i+1}/{len(StatWeightChart)}: DH={StatWeightChart['InitialDHWeight'][i]} Crit={StatWeightChart['InitialCritWeight'][i]} Det={StatWeightChart['InitialDetWeight'][i]} SS={StatWeightChart['InitialSSWeight'][i]}")

    # Calculate BiS
    Set = BiSLoop(MateriaFrame, Food, Set)

    # Get item string for each gear slot
    for slot in range(5, 16):
        StatWeightChart.at[i, slot] = ItemReturnString(MateriaFrame, Set[slot-4])

    # Get attributes for food
    Attributes = Food.Apply(MateriaFrame, Set, Food)

    # Get attribute values for each food slot
    for slot in range(16, 24):
        StatWeightChart.at[i, slot] = Attributes[slot-15]

# Sort by DPS column
StatWeightChart = StatWeightChart.sort_values('DPS', ascending=False)

# Write output to csv
OutputName = f"GearSetOutcomes{GearFile}"
StatWeightChart[~(StatWeightChart.iloc[:, 17:24].duplicated())].iloc[:, 5:24].to_csv(f"{OutputName}.csv", index=False)

# Clean up variables
del GearFile, MateriaFrame, Menu, Food, StatWeightChart, i, slot, Attributes, Set, OutputName
