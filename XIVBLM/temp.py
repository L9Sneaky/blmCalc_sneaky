import pandas as pd
import XIVBLM_py.dpsCalc as dpsCalc

ChartDict = pd.read_csv("XIVBLM/gear 6.4 data/Gear_6.4_GearSetOutcomes.csv")
statTable = dpsCalc.TablesCompare()
for i in range(len(ChartDict)):
    if ((ChartDict.iloc[i]['DH'] in statTable['DH']) + (ChartDict.iloc[i]['Crit'] in statTable['Crit'])
        + (ChartDict.iloc[i]['Det'] in statTable['Det']) + (ChartDict.iloc[i]['SS'] in statTable['SS'])) != 5:
        print(ChartDict.iloc[i])
        if ChartDict.iloc[i]['DH'] in statTable['DH']:
            print("DH is on point")
        if ChartDict.iloc[i]['Crit'] in statTable['Crit']:
            print("Crit is on point")
        if ChartDict.iloc[i]['Det'] in statTable['Det']:
            print("Det is on point")
        if ChartDict.iloc[i]['SS'] in statTable['SS']:
            print("SS is on point")
        print(f"DH Rate: {dpsCalc.CalcDHRate(ChartDict.iloc[i]['DH'])}")
        print(f"Crit Rate: {dpsCalc.CalcCritRate(ChartDict.iloc[i]['Crit'])}")
        print(f"Crit Damage: {dpsCalc.CalcCritDamage(ChartDict.iloc[i]['Crit'])}")
        print(f"Det: {dpsCalc.CalcDetDamage(ChartDict.iloc[i]['Det'])}")
        print(f"SS 2.5s: {dpsCalc.GcdCalc(2500,ChartDict.iloc[i]['SS'], False)}s")
        print(f"SS 2.8s: {dpsCalc.GcdCalc(2800,ChartDict.iloc[i]['SS'], False)}s")
        print(f"SS 3.0s: {dpsCalc.GcdCalc(3000,ChartDict.iloc[i]['SS'], False)}s")
        print("With LL")
        print(f"SS 2.5s: {dpsCalc.GcdCalc(2500,ChartDict.iloc[i]['SS'], True)}s")
        print(f"SS 2.8s: {dpsCalc.GcdCalc(2800,ChartDict.iloc[i]['SS'], True)}s")
        print(f"SS 3.0s: {dpsCalc.GcdCalc(3000,ChartDict.iloc[i]['SS'], True)}s")
        print()
# print(df)