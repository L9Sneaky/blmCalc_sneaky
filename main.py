# %%
from dpsCalc import Damage
from finalCalc import finalResult2
from itertools import product
import pandas as pd
import pickle
import numpy as np
import psutil
import gc
import sqlite3 as sql
from heapq import nlargest
# %%

baseStat = {'WD': 0, 'Int': 447, 'DH': 400,
            'Crit': 400, 'Det': 390, 'Sps': 400}

statKeys = ['DH', 'Crit', 'Det', 'Sps']

gearType = ['Weapon', 'Head', 'Body', 'Hand', 'Legs', 'Feet', 'Earing','Necklace', 'Bracelet', 'Left Ring', 'Right Ring']

wepDic = [{'Name': 'Asphodelos Staff', 'Type': 'Weapon', 'WD': 120,
           'Int': 304, 'DH': 0, 'Crit': 188, 'Det': 0, 'Sps': 269,
           'Slots': 2, 'MaxStat': 269},
          ]

wepDic2 = [
          {'Name': 'Ultimate Staff', 'Type': 'Weapon', 'WD': 120,
           'Int': 304, 'DH': 0, 'Crit': 188, 'Det': 0, 'Sps': 269,
           'Slots': 3, 'MaxStat': 269}
          ]

headDic = [{'Name': 'Asphodelos Headgear of Casting', 'Type': 'Head',
            'Int': 180, 'DH': 113, 'Crit': 162, 'Det': 0, 'Sps': 0,
            'Slots': 2, 'MaxStat': 162},
           {'Name': 'Augmented Radiant\'s Visor of Casting', 'Type': 'Head',
            'Int': 180, 'DH': 0, 'Crit': 0, 'Det': 113, 'Sps': 162,
            'Slots': 2, 'MaxStat': 162}
           ]

bodyDic = [{'Name': 'Asphodelos Chiton of Casting ', 'Type': 'Body',
            'Int': 285, 'DH': 0, 'Crit': 257, 'Det': 180, 'Sps': 0,
            'Slots': 2, 'MaxStat': 257},
           {'Name': 'Augmented Radiant\'s Mail of Casting', 'Type': 'Body',
            'Int': 285, 'DH': 257, 'Crit': 0, 'Det': 0, 'Sps': 180,
            'Slots': 2, 'MaxStat': 257}
           ]

handDic = [{'Name': 'Asphodelos Wristbands of Casting', 'Type': 'Hand',
            'Int': 180, 'DH': 0, 'Crit': 162, 'Det': 113, 'Sps': 0,
            'Slots': 2, 'MaxStat': 162},
           {'Name': 'Augmented Radiant\'s Gloves of Casting', 'Type': 'Hand',
            'Int': 180, 'DH': 113, 'Crit': 0, 'Det': 0, 'Sps': 162,
            'Slots': 2, 'MaxStat': 162}
           ]

legsDic = [{'Name': 'Asphodelos Trousers of Casting', 'Type': 'Legs',
            'Int': 285, 'DH': 0, 'Crit': 0, 'Det': 180, 'Sps': 257,
            'Slots': 2, 'MaxStat': 257},
           {'Name': 'Augmented Radiant\'s Hose of Casting', 'Type': 'Legs',
            'Int': 285, 'DH': 0, 'Crit': 180, 'Det': 257, 'Sps': 0,
            'Slots': 2, 'MaxStat': 257}
           ]

feetDic = [{'Name': 'Asphodelos Gaiters of Casting', 'Type': 'Feet',
            'Int': 180, 'DH': 162, 'Crit': 0, 'Det': 0, 'Sps': 113,
            'Slots': 2, 'MaxStat': 162},
           {'Name': 'Augmented Radiant\'s Greaves of Casting', 'Type': 'Feet',
            'Int': 180, 'DH': 113, 'Crit': 162, 'Det': 0, 'Sps': 0,
            'Slots': 2, 'MaxStat': 162}
           ]

eariDic = [{'Name': 'Asphodelos Earrings of Casting', 'Type': 'Earing',
            'Int': 142, 'DH': 127, 'Crit': 0, 'Det': 0, 'Sps': 89,
            'Slots': 2, 'MaxStat': 127},
           {'Name': 'Augmented Radiant\'s Earrings of Casting', 'Type': 'Earing',
            'Int': 142, 'DH': 0, 'Crit': 89, 'Det': 127, 'Sps': 0,
            'Slots': 2, 'MaxStat': 127}
           ]

neckDic = [{'Name': 'Asphodelos Necklace of Casting', 'Type': 'Necklace',
            'Int': 142, 'DH': 89, 'Crit': 127, 'Det': 0, 'Sps': 0,
            'Slots': 2, 'MaxStat': 127},
           {'Name': 'Augmented Radiant\'s Choker of Casting', 'Type': 'Necklace',
            'Int': 142, 'DH': 0, 'Crit': 0, 'Det': 127, 'Sps': 89,
            'Slots': 2, 'MaxStat': 127}
           ]

bracDic = [{'Name': 'Asphodelos Amulet of Casting', 'Type': 'Bracelet',
            'Int': 142, 'DH': 0, 'Crit': 0, 'Det': 89, 'Sps': 127,
            'Slots': 2, 'MaxStat': 127},
           {'Name': 'Augmented Radiant\'s Bracelet of Casting', 'Type': 'Bracelet',
            'Int': 142, 'DH': 89, 'Crit': 127, 'Det': 0, 'Sps': 0,
            'Slots': 2, 'MaxStat': 127}
           ]

lrinDic = [{'Name': 'Asphodelos Ring of Casting', 'Type': 'Left Ring',
            'Int': 142, 'DH': 0, 'Crit': 0, 'Det': 127, 'Sps': 89,
            'Slots': 2, 'MaxStat': 127}
           ]

rrinDic = [{'Name': 'Augmented Radiant\'s Ring of Casting', 'Type': 'Right Ring',
            'Int': 142, 'DH': 89, 'Crit': 127, 'Det': 0, 'Sps': 0,
            'Slots': 2, 'MaxStat': 127}
           ]

foodDic = [{'Name': 'Archon Burger',
            'DH': 1.1, 'Crit': 0, 'Det': 1.1, 'Sps': 0,
            'MaxDH': 90, 'MaxCrit': 0, 'MaxDet': 54, 'MaxSps': 0},
           {'Name': 'Pumpkin Potage',
            'DH': 0, 'Crit': 1.1, 'Det': 1.1, 'Sps': 0,
            'MaxDH': 0, 'MaxCrit': 54, 'MaxDet': 90, 'MaxSps': 0},
           {'Name': 'Sykon Cookie',
            'DH': 1.1, 'Crit': 0, 'Det': 0, 'Sps': 1.1,
            'MaxDH': 54, 'MaxCrit': 0, 'MaxDet': 0, 'MaxSps': 90},
           {'Name': 'Thavnarian Chai',
            'DH': 0, 'Crit': 1.1, 'Det': 0, 'Sps': 1.1,
            'MaxDH': 0, 'MaxCrit': 90, 'MaxDet': 0, 'MaxSps': 54}
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
    if num == 2:
        for i in statKeys:
            for j in statKeys:
                if [j, i] in posibleMeldSets:
                    pass
                else:
                    posibleMeldSets.append([i, j])
    if num == 3:
        for i in statKeys:
            for j in statKeys:
                for k in statKeys:
                    if (([j, i, k] in posibleMeldSets
                         or [k, j, i] in posibleMeldSets
                         or [i, k, j] in posibleMeldSets
                         or [j, k, i] in posibleMeldSets
                         or [k, i, j] in posibleMeldSets
                         or [i, j, k] in posibleMeldSets)):
                        pass
                    else:
                        posibleMeldSets.append([i, j, k])
    return posibleMeldSets

def getEveryMeld(Gear):
    baseMeldStat = {'DH': 0, 'Crit': 0, 'Det': 0, 'Sps': 0}
    meldedGear = []
    for item in range(len(Gear)):
        meldSlot = Gear[item]['Slots']
        avalableMelds = getAllMeldOption(Gear[item]['Slots'])
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
            for stat in statKeys:
                tempGearStat[stat] += tempStat[stat]
            if (tempGearStat['DH'] > tempGearStat['MaxStat']
                or tempGearStat['Crit'] > tempGearStat['MaxStat']
                or tempGearStat['Det'] > tempGearStat['MaxStat']
                or tempGearStat['Sps'] > tempGearStat['MaxStat']
                ):
                pass
            else:
                del tempGearStat["Slots"]
                del tempGearStat["MaxStat"]
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
        if(foodDic[i][first] == 90 and foodDic[i][second] == 54):
            best = foodDic[i]
    if best == 0:
        for i in range(len(foodDic)):
            if (foodDic[i][first] == 90):
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
    return [wepDic[0],
            headDic[0],
            bodyDic[0],
            handDic[0],
            legsDic[0],
            feetDic[0],
            eariDic[0],
            neckDic[0],
            bracDic[0],
            lrinDic[0],
            rrinDic[0]
            ]


def damageGainOverBaseSet(stat, crit: bool=False):
    _, tpps = getAvgDamage(getGearStat(baseStat.copy(), unmeldedRaidGear()),crit)
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

# %%

def test(*args, crit: bool=False):
    crit = 1 if crit else 0
    bestgear = []
    for seq in args:
        temp = []
        # print(bestgear)
        item = getEveryMeld(seq)
        for i in range(len(item)):
            copy = bestgear.copy()
            copy.append(item[i])

            stat = getGearStat(baseStat.copy(), copy)
            damage = getAvgDamage(stat,crit)
            gain = damageGainOverBaseSet(damage,crit)

            temp.append(gain)
            # temp.append(damage[1])
        bestgear.append(item[np.argmax(temp)])
    return bestgear


crit = False
best = test(wepDic2, headDic, bodyDic,
            handDic, legsDic, feetDic,
            eariDic, neckDic, bracDic,
            lrinDic, rrinDic, crit=crit)


stato = getGearStat(baseStat.copy(), best)
food = findBestFood(stato)
stat = statWithFood(stato, food)
damage = getAvgDamage(stat,crit)
gain = damageGainOverBaseSet(damage,crit)

stato, stat, food['Name'], damage, gain

# %%

# %%

def test2(*args,crit=0):
    crit = 1 if crit else 0
    start = getEveryMeld(args[0])
    bestgear2 = []
    for i in start:
        bestgear = [i]
        bestgearcrit = [i]
        bestgeardh = [i]
        bestgeardet = [i]
        bestgearsps = [i]
        for seq in args[1:]:
            tempgain = []
            tempcrit = []
            tempdh = []
            tempdet = []
            tempsps = []
            item = getEveryMeld(seq)
            for i in range(len(item)):
                copy = bestgear.copy()
                copy.append(item[i])

                stat = getGearStat(baseStat.copy(), copy)
                damage = getAvgDamage(stat,crit)
                gain = damageGainOverBaseSet(damage,crit)
                tempgain.append(gain)
                tempcrit.append(stat['Crit'])
                tempdh.append(stat['DH'])
                tempdet.append(stat['Det'])
                tempsps.append(stat['Sps'])
            bestgear.append(item[np.argmax(tempgain)])
            bestgearcrit.append(item[np.argmax(tempcrit)])
            bestgeardh.append(item[np.argmax(tempdh)])
            bestgeardet.append(item[np.argmax(tempdet)])
            bestgearsps.append(item[np.argmax(tempsps)])
        bestgear2.append(bestgear)
        bestgear2.append(bestgearcrit)
        bestgear2.append(bestgeardh)
        bestgear2.append(bestgeardet)
        bestgear2.append(bestgearsps)
    return bestgear2

crit = 0
eh = test2(wepDic, headDic, bodyDic,
           handDic, legsDic, feetDic,
           eariDic, neckDic, bracDic,
           lrinDic, rrinDic, crit=crit)



new = []
for i in range(len(eh)):
    for food in foodDic:
        stato = getGearStat(baseStat.copy(), eh[i])
        # food = findBestFood(stato)
        stat = statWithFood(stato, food)
        damage = getAvgDamage(stat,crit)
        gain = damageGainOverBaseSet(damage,crit)

        a = statsToArray(stat)
        a.extend(pd.DataFrame(eh[i])['Name'].to_numpy().tolist())
        a.append(food['Name'])
        a.extend(damage)
        a.append(gain)
        new.append(a)

pd.set_option('display.max_columns', None)
df = pd.DataFrame(new,columns=(['WD', 'Int', 'DH', 'Crit', 'Det', 'Sps', 'Weapon', 'Head', 'Body', 'Hands', 'Legs', 'Feet', 'Earing', 'Necklace', ' Bracelet', 'Left Ring', 'Right Ring', 'Food', 'Fire Proc', 'Thunder Proc', 'Gain']))
df.drop_duplicates().sort_values('Gain', ascending=False, ignore_index=True)
df.to_csv('test2.csv', index=False)
# %%
