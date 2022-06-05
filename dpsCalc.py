import math as Math
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


# Pulled from Orinx's Gear Comparison Sheet with slight modifications
def Damage(Potency, WD, JobMod, MainStat, Det, Crit, DH, SS, TEN, hasBrd, hasDrg, hasSch, hasDnc, classNum):
    MainStat = Math.floor(MainStat*(1+0.01*classNum))
    Damage = Math.floor(Potency*(WD+Math.floor(baseMain*JobMod/1000))*(100+Math.floor((MainStat-baseMain)*195/baseMain))/100)
    Damage = Math.floor(Damage*(1000+Math.floor(140*(Det-baseMain)/levelMod))/1000)
    Damage = Math.floor(Damage*(1000+Math.floor(100*(TEN-baseSub)/levelMod))/1000)
    Damage = Math.floor(Damage*(1000+Math.floor(130*(SS-baseSub)/levelMod))/1000/100)
    Damage = Math.floor(Damage*magicAndMend)
    Damage = Math.floor(Damage*enochian)
    CritDamage = CalcCritDamage(Crit)
    CritRate = CalcCritRate(Crit) + (battleLitanyAvg if hasDrg else 0) + (chainStratAvg if hasSch else 0) + (devilmentAvg if hasDnc else 0) + (brdCritAvg if hasBrd else 0)
    DHRate = CalcDHRate(DH) + (battleVoiceAvg + brdDhAvg if hasBrd else 0) + (devilmentAvg if hasDnc else 0)
    TotalDamage = Damage * ((1+(DHRate/4))*(1+(CritRate*CritDamage)))
    return TotalDamage


def CalcCritRate(Crit):
    return Math.floor((200*(Crit-baseSub)/levelMod+50))/1000


def CalcCritDamage(Crit):
    return (Math.floor(200*(Crit-baseSub)/levelMod+400))/1000


def CalcDHRate(DH):
    return Math.floor(550*(DH-baseSub)/levelMod)/1000


def CalcDetDamage(Det):
    return (1000+Math.floor(140*(Det-baseMain)/levelMod))/1000


def CalcDamage(Potency, Multiplier, CritDamageMult, CritRate, DHRate) :
    Damage = Potency * Multiplier
    DHDamage = 1.25 * Damage
    CritDamage = CritDamageMult * Damage
    CritDHDamage = CritDamageMult * 1.25 * Damage
    CritDHRate = CritRate * DHRate
    NormalRate = 1-CritRate-DHRate+CritDHRate

    return Damage * NormalRate + CritDamage * (CritRate-CritDHRate) + DHDamage * (DHRate-CritDHRate) + CritDHDamage * CritDHRate
