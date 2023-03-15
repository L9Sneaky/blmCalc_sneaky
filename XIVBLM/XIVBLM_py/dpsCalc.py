import numpy as np
from XIVBLM_py.oldPpsCalc import FirePps, ThunderPps
# Party buff things
battleVoiceAvg = (15 / 120) * 0.2
battleLitanyAvg = (15 / 120) * 0.1
chainStratAvg = (15 / 120) * 0.1
devilmentAvg = (20 / 120) * 0.2
brdCritAvg = (45/120) * 0.02
brdDhAvg = (45/120) * 0.03

# Traits and eno
magicAndMend = 1.3
enochian = 1.2

# jobmod etc

levelMod = 1900
baseMain = 390
baseSub = 400


def DPS(WD, Int, DH, Crit, Det, SS, TEN=400, hasBrd=False, hasDrg=False, hasSch=False, hasDnc=False, classNum=5):
  Potency = FirePps(SS)
  JobMod = 115
  Int = np.floor(Int * (1 + 0.01 * classNum))
  Damage = np.floor(Potency * (WD + np.floor(baseMain * JobMod / 1000)) * (100 + np.floor((Int - baseMain) * 195 / baseMain)) / 100)
  Damage = np.floor(Damage * (1000 + np.floor(140 * (Det - baseMain) / levelMod)) / 1000)
  Damage = np.floor(Damage * (1000 + np.floor(100 * (TEN - baseSub) / levelMod)) / 1000)
  Damage = np.floor(Damage * (1000 + np.floor(130 * (400 - baseSub) / levelMod)) / 1000 / 100)
  Damage = np.floor(Damage * magicAndMend)
  Damage = np.floor(Damage * enochian)
  CritDamage = CalcCritDamage(Crit)
  CritRate = CalcCritRate(Crit) + (hasDrg * battleLitanyAvg) + (hasSch * chainStratAvg) + (hasDnc * devilmentAvg) + (hasBrd * brdCritAvg)
  DHRate = CalcDHRate(DH) + (hasBrd * (battleVoiceAvg + brdDhAvg)) + (hasDnc * devilmentAvg)
  return Damage * ((1 + (DHRate / 4)) * (1 + (CritRate * CritDamage)))

def CalcCritRate(Crit):
  return np.floor((200 * (Crit - baseSub) / levelMod + 50)) / 1000

def CalcCritDamage(Crit):
  return (np.floor(200 * (Crit - baseSub) / levelMod + 400)) / 1000

def CalcDHRate(DH):
  return np.floor(550 * (DH - baseSub) / levelMod) / 1000

def CalcDetDamage(Det):
  return (1000 + np.floor(140 * (Det - baseMain) / levelMod)) / 1000


def CalcCritRate(Crit):
    return np.floor((200*(Crit-baseSub)/levelMod+50))/1000


def CalcCritDamage(Crit):
    return (np.floor(200*(Crit-baseSub)/levelMod+400))/1000


def CalcDHRate(DH):
    return np.floor(550*(DH-baseSub)/levelMod)/1000


def CalcDetDamage(Det):
    return (1000+np.floor(140*(Det-baseMain)/levelMod))/1000


def CalcDamage(Potency, Multiplier, CritDamageMult, CritRate, DHRate) :
    Damage = Potency * Multiplier
    DHDamage = 1.25 * Damage
    CritDamage = CritDamageMult * Damage
    CritDHDamage = CritDamageMult * 1.25 * Damage
    CritDHRate = CritRate * DHRate
    NormalRate = 1-CritRate-DHRate+CritDHRate

    return Damage * NormalRate + CritDamage * (CritRate-CritDHRate) + DHDamage * (DHRate-CritDHRate) + CritDHDamage * CritDHRate

def Damage2(Potency, WD, JobMod, Int, Det, Crit, DH, SS, TEN, hasBrd, hasDrg, hasSch, hasDnc, classNum):
    Int = np.floor(Int*(1+0.01*classNum))
    Damage = np.floor(Potency*(WD+np.floor(baseMain*JobMod/1000))*(100+np.floor((Int-baseMain)*195/baseMain))/100)
    Damage = np.floor(Damage*(1000+np.floor(140*(Det-baseMain)/levelMod))/1000)
    Damage = np.floor(Damage*(1000+np.floor(100*(TEN-baseSub)/levelMod))/1000)
    Damage = np.floor(Damage*(1000+np.floor(130*(SS-baseSub)/levelMod))/1000/100)
    Damage = np.floor(Damage*magicAndMend)
    Damage = np.floor(Damage*enochian)
    CritDamage = CalcCritDamage(Crit)
    CritRate = CalcCritRate(Crit) + (battleLitanyAvg if hasDrg else 0) + (chainStratAvg if hasSch else 0) + (devilmentAvg if hasDnc else 0) + (brdCritAvg if hasBrd else 0)
    DHRate = CalcDHRate(DH) + (battleVoiceAvg + brdDhAvg if hasBrd else 0) + (devilmentAvg if hasDnc else 0)
    TotalDamage = Damage * ((1+(DHRate/4))*(1+(CritRate*CritDamage)))
    return TotalDamage