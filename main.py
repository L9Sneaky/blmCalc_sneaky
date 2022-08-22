# %%
import itertools
from dpsCalc import Damage
from finalCalc import finalResult2
import pandas as pd
import pickle
import numpy as np
from heapq import nlargest
# %%

baseStat = {'WD': 0, 'Int': 447, 'DH': 400,
            'Crit': 400, 'Det': 390, 'Sps': 400}

statKeys = ['DH', 'Crit', 'Det', 'Sps']

gearType = ['Weapon', 'Head', 'Body', 'Hand', 'Legs', 'Feet', 'Earing','Necklace', 'Bracelet', 'Left Ring', 'Right Ring']

# %%

wepDic=[
        {'id': 35254,
        'Name': 'Asphodelos Staff', 'Type': 'Weapon', 'WD': 120,
        'Int': 304, 'DH': 0, 'Crit': 188, 'Det': 0, 'Sps': 269,
        'Slots': 2, 'MaxStat': 269, 'AM': False}
        ]

wepDic2=[
        {'id': 36952,
        'Name': 'Ultimate Staff', 'Type': 'Weapon', 'WD': 120,
        'Int': 304, 'DH': 0, 'Crit': 188, 'Det': 0, 'Sps': 269,
        'Slots': 3, 'MaxStat': 269, 'AM': False}
        ]

wepDic3=[
        {'id': 0,
        'Name': 'Classical Longpole', 'Type': 'Weapon', 'WD': 115,
        'Int': 266, 'DH': 0, 'Crit': 253, 'Det': 0, 'Sps': 177,
        'Slots': 2, 'MaxStat': 253, 'AM': True}
        ]

wepDicR=[
        {'id': 'relic',
        'Name': 'Blades Fury', 'Type': 'Weapon', 'WD': 125,
        'Int': 306, 'DH': 172, 'Crit': 0, 'Det': 126, 'Sps': 170,
        'Slots': 5, 'MaxStat': 999, 'AM': True}
        ]

headDic=[
        {'id': 35295,
        'Name': 'Asphodelos Headgear of Casting', 'Type': 'Head',
        'Int': 180, 'DH': 113, 'Crit': 162, 'Det': 0, 'Sps': 0,
        'Slots': 2, 'MaxStat': 162, 'AM': False},
        {'id': 35220,
        'Name': 'Augmented Radiant\'s Visor of Casting', 'Type': 'Head',
        'Int': 180, 'DH': 0, 'Crit': 0, 'Det': 113, 'Sps': 162,
        'Slots': 2, 'MaxStat': 162, 'AM': False}
        ]

bodyDic=[
        {'id': 35296,
        'Name': 'Asphodelos Chiton of Casting', 'Type': 'Body',
        'Int': 285, 'DH': 0, 'Crit': 257, 'Det': 180, 'Sps': 0,
        'Slots': 2, 'MaxStat': 257, 'AM': False},
        {'id': 35220,
        'Name': 'Augmented Radiant\'s Mail of Casting', 'Type': 'Body',
        'Int': 285, 'DH': 257, 'Crit': 0, 'Det': 0, 'Sps': 180,
        'Slots': 2, 'MaxStat': 257, 'AM': False}
        ]

bodyDic1=[
        {'id': 1,
        'Name': 'Ornate Classical Signifer\'s Chiton', 'Type': 'Body',
        'Int': 256, 'DH': 171, 'Crit': 0, 'Det': 244, 'Sps': 0,
        'Slots': 5, 'MaxStat': 244, 'AM': False}
        ]

handDic=[
        {'id':35297,
        'Name': 'Asphodelos Wristbands of Casting', 'Type': 'Hand',
        'Int': 180, 'DH': 0, 'Crit': 162, 'Det': 113, 'Sps': 0,
        'Slots': 2, 'MaxStat': 162, 'AM': False},
       {'id': 35222,
        'Name': 'Augmented Radiant\'s Gloves of Casting', 'Type': 'Hand',
        'Int': 180, 'DH': 113, 'Crit': 0, 'Det': 0, 'Sps': 162,
        'Slots': 2, 'MaxStat': 162, 'AM': False}
        ]

legsDic=[
        {'id': 35298,
        'Name': 'Asphodelos Trousers of Casting', 'Type': 'Legs',
        'Int': 285, 'DH': 0, 'Crit': 0, 'Det': 180, 'Sps': 257,
        'Slots': 2, 'MaxStat': 257, 'AM': False},
       {'id': 35223,
        'Name': 'Augmented Radiant\'s Hose of Casting', 'Type': 'Legs',
        'Int': 285, 'DH': 0, 'Crit': 180, 'Det': 257, 'Sps': 0,
        'Slots': 2, 'MaxStat': 257, 'AM': False}
           ]

feetDic=[
        {'id': 35299,
        'Name': 'Asphodelos Gaiters of Casting', 'Type': 'Feet',
        'Int': 180, 'DH': 162, 'Crit': 0, 'Det': 0, 'Sps': 113,
        'Slots': 2, 'MaxStat': 162, 'AM': False},
       {'id': 35224,
        'Name': 'Augmented Radiant\'s Greaves of Casting', 'Type': 'Feet',
        'Int': 180, 'DH': 113, 'Crit': 162, 'Det': 0, 'Sps': 0,
        'Slots': 2, 'MaxStat': 162, 'AM': False}
        ]

eariDic=[
        {'id': 35304,
        'Name': 'Asphodelos Earrings of Casting', 'Type': 'Earing',
        'Int': 142, 'DH': 127, 'Crit': 0, 'Det': 0, 'Sps': 89,
        'Slots': 2, 'MaxStat': 127, 'AM': False},
        {'id': 35229,
        'Name': 'Augmented Radiant\'s Earrings of Casting', 'Type': 'Earing',
        'Int': 142, 'DH': 0, 'Crit': 89, 'Det': 127, 'Sps': 0,
        'Slots': 2, 'MaxStat': 127, 'AM': False}
        ]

neckDic=[
        {'id': 35309,
        'Name': 'Asphodelos Necklace of Casting', 'Type': 'Necklace',
        'Int': 142, 'DH': 89, 'Crit': 127, 'Det': 0, 'Sps': 0,
        'Slots': 2, 'MaxStat': 127, 'AM': False},
        {'id': 35234,
        'Name': 'Augmented Radiant\'s Choker of Casting', 'Type': 'Necklace',
        'Int': 142, 'DH': 0, 'Crit': 0, 'Det': 127, 'Sps': 89,
        'Slots': 2, 'MaxStat': 127, 'AM': False}
        ]

bracDic=[
        {'id': 35314,
        'Name': 'Asphodelos Amulet of Casting', 'Type': 'Bracelet',
        'Int': 142, 'DH': 0, 'Crit': 0, 'Det': 89, 'Sps': 127,
        'Slots': 2, 'MaxStat': 127, 'AM': False},
        {'id': 35239,
        'Name': 'Augmented Radiant\'s Bracelet of Casting', 'Type': 'Bracelet',
        'Int': 142, 'DH': 89, 'Crit': 127, 'Det': 0, 'Sps': 0,
        'Slots': 2, 'MaxStat': 127, 'AM': False}
        ]

lrinDic=[
        {'id': 35319,
        'Name': 'Asphodelos Ring of Casting', 'Type': 'Left Ring',
        'Int': 142, 'DH': 0, 'Crit': 0, 'Det': 127, 'Sps': 89,
        'Slots': 2, 'MaxStat': 127, 'AM': False}
        ]

rrinDic=[
        {'id': 35244,
        'Name': 'Augmented Radiant\'s Ring of Casting', 'Type': 'Right Ring',
        'Int': 142, 'DH': 89, 'Crit': 127, 'Det': 0, 'Sps': 0,
        'Slots': 2, 'MaxStat': 127, 'AM': False}
        ]

foodDic=[
        {'Name': 'Archon Burger',
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
            a = itertools.product(getAllMeldOption(meldSlot), getAllMeldOption(2))
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
crit = 0
best = test(wepDicR, headDic, bodyDic1,
            handDic, legsDic, feetDic,
            eariDic, neckDic, bracDic,
            lrinDic, rrinDic, crit=crit)


stato = getGearStat(baseStat.copy(), best)
food = findBestFood(stato)
stat = statWithFood(stato, food)
damage = getAvgDamage(stat,crit)
gain = damageGainOverBaseSet(damage,crit)

stat, food['Name'], damage, gain

# %%
pd.DataFrame(best)
best[0]['Name']









# %%
