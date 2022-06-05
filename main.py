import tensorflow as tf
from dpsCalc import Damage
from finalCalc import finalResult2
from itertools import product
import tensorflow as tf
import pandas as pd
import pickle
import numpy as np
import psutil
import gc
import sqlite3 as sql

# %%

baseStat = {'WD': 0, 'Int': 447, 'DH': 400,
            'Crit': 400, 'Det': 390, 'Sps': 400}
statKeys = ['DH', 'Crit', 'Det', 'Sps']

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
            'MaxDH': 93, 'MaxCrit': 0, 'MaxDet': 54, 'MaxSps': 0},
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
def getAvgDamage(GearStat, hasBrd=0, hasDrg=0, hasSch=0, hasDnc=0):
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
                meldedGear.append(tempGearStat)
    print(len(meldedGear))
    return meldedGear


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

def damageGainOverBaseSet(stat):
    _, tpps = getAvgDamage(getGearStat(baseStat.copy(), unmeldedRaidGear()))
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

# %%

def getAllGear(weplist, headlist, bodylist, handlist, legslist, feetlist, earilist, necklist, braclist, lrinlist, rrinlist, foodlist):
    columns = ['WD','Int','DH','Crit','Det','Sps','Fire pps','Thunder pps','Gain','Weapon','Head','Body','Hand','Legs','Feet','Earrings','Necklace','Bracelet','Left Ring','Right Ring','Food']
    gc.collect()
    char = baseStat.copy()
    Gear = []
    i = 0
    n = 0
    for sequnce in product(weplist, headlist, bodylist,
                           handlist, legslist, feetlist,
                           earilist, necklist, braclist,
                           lrinlist, rrinlist, foodlist
                           ):

        stats = getGearStat(char, sequnce[0:-1])
        statswithfood = statWithFood(stats, sequnce[-1])
        damage = getAvgDamage(statswithfood)
        gain = damageGainOverBaseSet(damage)
        temp = statsToArray(statswithfood)

        Gear.append([
                    temp[0], temp[1], temp[2],
                    temp[3], temp[4], temp[5],
                    damage[0], damage[1], gain,
                    sequnce[0]['Name'], sequnce[1]['Name'], sequnce[2]['Name'],
                    sequnce[3]['Name'], sequnce[4]['Name'], sequnce[5]['Name'],
                    sequnce[6]['Name'], sequnce[7]['Name'], sequnce[8]['Name'],
                    sequnce[9]['Name'],sequnce[10]['Name'], sequnce[11]['Name']
                    ])
        n += 1
        if psutil.virtual_memory()[2] > 80:
            print('AYO mMEMORY OVER 80%')
            print('loop number ' + str(n) + ' out of 86400000000 ' + str(round(n/86400000000, 3)) + '% loops remaining ')
            pd.DataFrame(Gear, columns=columns).to_parquet('D:/data/' + 'X' + str(i) + '.gzip', index=False, compression='gzip')

            i += 1
            del Gear
            del stats
            del statswithfood
            del damage
            del gain
            del temp
            while True:
                gc.collect()
                if psutil.virtual_memory()[2] < 50:
                    break
            Gear = []

    pd.DataFrame(Gear, columns=columns).to_parquet('D:/data/' + 'X' + str(i) + '.gzip', index=False, compression='gzip')
    # return Gear

test = getAllGear(getEveryMeld(wepDic),
                  getEveryMeld(headDic),
                  getEveryMeld(bodyDic),
                  getEveryMeld(handDic),
                  getEveryMeld(legsDic),
                  getEveryMeld(feetDic),
                  getEveryMeld(eariDic),
                  getEveryMeld(neckDic),
                  getEveryMeld(bracDic),
                  getEveryMeld(lrinDic),
                  getEveryMeld(rrinDic),
                  foodDic
                )


# %%
gc.collect()
# %%

# %%
