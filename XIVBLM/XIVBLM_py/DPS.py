import numpy as np
import pandas as pd

def DPS(WD, Int, DH, Crit, Det, SS):
    SelfEsteem = np.floor(100 * PPS(SS) * damage_per_potency(WD, np.floor(Int * 1.05)))
    SelfEsteem = np.floor(SelfEsteem * Det_DPS(Det) / 100)
    SelfEsteem = np.floor(1.3 * SelfEsteem)
    SelfEsteem = np.floor(1.2 * SelfEsteem)
    return SelfEsteem * DH_DPS(DH) * Crit_DPS(Crit)


def DHRate(DirectHit=400):
    return np.floor(550*(DirectHit-400)/1900)/1000

def DH_DPS(DirectHit=400):
    return 1+DHRate(DirectHit)/4

def Crit_Rate(crit=400):
    return np.floor((200 * (crit - 400) / 1900 + 50)) / 1000

def Crit_Bonus(crit=400):
    return np.floor(200 * (crit - 400) / 1900 + 400) / 1000

def Crit_DPS(crit=400):
    return 1 + Crit_Rate(crit) * Crit_Rate(crit)

def Det_DPS(Det=390):
    return 1 + (140 * (Det - 390) // 1900) / 1000

PPSTable = pd.read_csv('XIVBLM/Tables/PPSTable.csv')

def PPS(SS=400, Crit=400):
    Tier = np.argmax(PPSTable["SpS"] > SS)
    return PPSTable["PPS"][Tier]

def damage_per_potency(WD=111, Int=447):
    return (1/100) * (WD + (390*115/1000)) * ((100 + (Int - 390)*195/390)/100)
