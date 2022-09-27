# %%.keys(t['Type'].unique())
import itertools
from dpsCalc import Damage
from finalCalc import finalResult2
from etroGetter import get_set_from_etro
import pandas as pd
import pickle
import numpy as np
from heapq import nlargest
import yaml
# %%

baseStat = {'WD': 0, 'Int': 447, 'DH': 400,
            'Crit': 400, 'Det': 390, 'Sps': 400}

statKeys = ['DH', 'Crit', 'Det', 'Sps']

gearType = ['Weapon', 'Head', 'Body', 'Hand', 'Legs', 'Feet', 'Earing','Necklace', 'Bracelet', 'Left Ring', 'Right Ring']

# %%
foodDic=[
        {'Name': 'Carrot Pudding',
        'DH': 0, 'Crit': 1.1, 'Det': 1.1, 'Sps': 0,
        'MaxDH': 0, 'MaxCrit': 58, 'MaxDet': 97, 'MaxSps': 0},
        {'Name': 'Garlean Pizza',
        'DH': 0, 'Crit': 1.1, 'Det': 0, 'Sps': 1.1,
        'MaxDH': 0, 'MaxCrit': 97, 'MaxDet': 0, 'MaxSps': 58},
        {'Name': 'Melon Pie',
        'DH': 1.1, 'Crit': 0, 'Det': 1.1, 'Sps': 0,
        'MaxDH': 97, 'MaxCrit': 0, 'MaxDet': 58, 'MaxSps': 90},
        {'Name': 'Piennolo Tomato Salad',
        'DH': 0, 'Crit': 0, 'Det': 1.1, 'Sps': 1.1,
        'MaxDH': 0, 'MaxCrit': 0, 'MaxDet': 58, 'MaxSps': 97}
        ]


# %%

def getAvgDamage(GearStat,crit: bool=False):
    if crit:
        hasBrd=1
        hasDrg=1
        hasSch=1
        hasDnc=1
    else:
        hasBrd=0
        hasDrg=0
        hasSch=0
        hasDnc=0
    firePps, thunderPps = finalResult2(GearStat['Sps'])
    fireDamage = Damage(firePps, GearStat['WD'], 115, GearStat['Int'], GearStat['Det'],
                        GearStat['Crit'], GearStat['DH'], 400, 400, hasBrd, hasDrg, hasSch, hasDnc, 5)
    thunderDamage = Damage(thunderPps, GearStat['WD'], 115, GearStat['Int'], GearStat['Det'],
                           GearStat['Crit'], GearStat['DH'], 400, 400, hasBrd, hasDrg, hasSch, hasDnc, 5)
    return fireDamage, thunderDamage


def getGearStat(charStat, gear):
    tempCharStat = charStat.copy()
    for j in range(len(gear)):
        for i in baseStat:
            try:
                tempCharStat[i] += gear[j][i]
            except Exception:
                pass
    return tempCharStat

def getAllMeldOption(num=0):
    posibleMeldSets = []
    p = itertools.combinations_with_replacement(statKeys, r=num)
    for i in p:
        posibleMeldSets.append([*i])
    return posibleMeldSets

def getEveryMeld(Gear):
    baseMeldStat = {'DH': 0, 'Crit': 0, 'Det': 0, 'Sps': 0}
    meldedGear = []
    for item in range(len(Gear)):
        AM = Gear[item]['AM']
        meldSlot = Gear[item]['Slots']
        avalableMelds = getAllMeldOption(meldSlot)
        if AM:
            meldSlot = min(meldSlot + 1, 5)
            avalableMelds = []
            a = itertools.product(getAllMeldOption(meldSlot), getAllMeldOption(5-meldSlot))
            for i in a:
                avalableMelds.append([*i[0], *i[1]])
        for option in range(len(avalableMelds)):
            tempStat = baseMeldStat.copy()
            tempGearStat = Gear[item].copy()
            for i in range(meldSlot):
                if avalableMelds[option][i] == 'DH':
                    tempGearStat['Name'] += ' DH'
                    tempStat['DH'] += 36
                if avalableMelds[option][i] == 'Crit':
                    tempGearStat['Name'] += ' Crit'
                    tempStat['Crit'] += 36
                if avalableMelds[option][i] == 'Det':
                    tempGearStat['Name'] += ' Det'
                    tempStat['Det'] += 36
                if avalableMelds[option][i] == 'Sps':
                    tempGearStat['Name'] += ' Sps'
                    tempStat['Sps'] += 36

            if AM:
                for i in range(meldSlot, 5):
                    if avalableMelds[option][i] == 'DH':
                        tempGearStat['Name'] += ' DH'
                        tempStat['DH'] += 12
                    if avalableMelds[option][i] == 'Crit':
                        tempGearStat['Name'] += ' Crit'
                        tempStat['Crit'] += 12
                    if avalableMelds[option][i] == 'Det':
                        tempGearStat['Name'] += ' Det'
                        tempStat['Det'] += 12
                    if avalableMelds[option][i] == 'Sps':
                        tempGearStat['Name'] += ' Sps'
                        tempStat['Sps'] += 12

            for stat in statKeys:
                tempGearStat[stat] += tempStat[stat]

            if (tempGearStat['DH'] > tempGearStat['MaxStat']
                or tempGearStat['Crit'] > tempGearStat['MaxStat']
                or tempGearStat['Det'] > tempGearStat['MaxStat']
                or tempGearStat['Sps'] > tempGearStat['MaxStat']):
                pass
            else:
                del tempGearStat["Slots"]
                del tempGearStat["MaxStat"]
                del tempGearStat["AM"]
                meldedGear.append(tempGearStat)
            # print(len(meldedGear))
    return meldedGear

def getHighiestStats(stat1,n=2):
    stat = statsToArray(stat1)[2:6]
    return [stat.index(i) for i in sorted(stat, reverse=True)][:n]

def findBestFood(stat1):
    best = 0
    a = getHighiestStats(stat1)
    first = 'Max'+statKeys[a[0]]
    second = 'Max'+statKeys[a[1]]
    for i in range(len(foodDic)):
        if(foodDic[i][first] == 97 and foodDic[i][second] == 58):
            best = foodDic[i]
    if best == 0:
        for i in range(len(foodDic)):
            if (foodDic[i][first] == 97):
                best = foodDic[i]
    return best

def statWithFood(Gear, Food):
    tempGear = Gear.copy()
    tempStat = {'DH': 0, 'Crit': 0, 'Det': 0, 'Sps': 0}
    for stat in statKeys:
        tempStat[stat] = Gear[stat] * Food[stat]
        if tempStat[stat] > Food['Max'+stat]:
            tempStat[stat] = Food['Max'+stat]
        tempGear[stat] += tempStat[stat]
    return tempGear

def unmeldedRaidGear():
    path = 'https://etro.gg/gearset/31b99419-45ea-43b9-9e99-fd5b611006d4''
    return get_set_from_etro(path)

baseset = unmeldedRaidGear()

def damageGainOverBaseSet(stat, crit: bool=False):
    _, tpps = getAvgDamage(baseset,crit)
    return ((stat[1]/tpps)-1)*100

def getGearNameList(gear):
    names = []
    for g in range(len(gear)):
        names.append(gear[g]['Name'])
    return names

def statsToArray(stat: dict):
    statlist = []
    for g in stat.keys():
        statlist.append(stat[g])
    return statlist

def all_equal(iterator):
    return len(set(iterator)) <= 1

# %%
def test(*args, crit: bool=False):
    crit = 1 if crit else 0
    bestgear = []
    for seq in args:
        temp = []
        temp2 = []
        # print(bestgear)
        item = getEveryMeld(seq)
        for i in range(len(item)):
            copy = bestgear.copy()
            copy.append(item[i])

            stat = getGearStat(baseStat.copy(), copy)
            damage = getAvgDamage(stat,crit)
            gain = damageGainOverBaseSet(damage,crit)
            temp2.append(stat['Crit'])
            temp.append(gain)

        if crit and not all_equal(temp2):
            bestgear.append(item[np.argmax(temp2)])
        else:
            bestgear.append(item[np.argmax(temp)])
    return bestgear

# %%
with open("Gear_6.2_preBis.yaml", 'r') as stream:
    gear = yaml.safe_load(stream)
# %%
gear.keys()
crit = 1

best = test(gear['Weapon'], gear['Head'], gear['Body'], gear['Hands'],
            gear['Legs'], gear['Feet'], gear['Earrings'], gear['Necklace'],
            gear['Bracelets'], gear['Ring'], gear['Ring'], crit = crit)

stato = getGearStat(baseStat.copy(), best)
food = findBestFood(stato)
stat = statWithFood(stato, food)
damage = getAvgDamage(stat,crit)
gain = damageGainOverBaseSet(damage,crit)




# %%
pd.DataFrame(best)
stat, food['Name'], damage, gain

# %%

best[7]['Name']
# %%
test = get_set_from_etro('https://etro.gg/gearset/73f9f3af-2fa1-4871-85a3-a0f6adbb5e28')
damage = getAvgDamage(test,crit)
gain = damageGainOverBaseSet(damage,crit)

test, damage, gain
unmeldedRaidGear()
