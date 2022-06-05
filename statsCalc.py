import math as Math
from dpsCalc import CalcDHRate, CalcCritRate, CalcCritDamage

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
def DamageVariance(Potency, WD, JobMod, MainStat, Det, Crit, DH, SS, TEN, hasBrd, hasDrg, hasSch, hasDnc, classNum):
    MainStat = Math.floor(MainStat*(1+0.01*classNum))
    DamageSum = Math.floor(Potency*(WD+Math.floor(baseMain*JobMod/1000))*(100+Math.floor((MainStat-baseMain)*195/baseMain))/100)
    DamageSum = Math.floor(DamageSum*(1000+Math.floor(140*(Det-baseMain)/levelMod))/1000)
    DamageSum = Math.floor(DamageSum*(1000+Math.floor(100*(TEN-baseSub)/levelMod))/1000)
    DamageSum = Math.floor(DamageSum*(1000+Math.floor(130*(SS-baseSub)/levelMod))/1000/100)
    DamageSum = Math.floor(DamageSum*magicAndMend)
    DamageSum = Math.floor(DamageSum*enochian)
    CritDamage = Math.floor(DamageSum*(1000 * (1+CalcCritDamage(Crit)))/1000)
    DHDamage = Math.floor(DamageSum*1250/1000)
    CritDHDamage = (CritDamage*1250/1000)
    CritRate = CalcCritRate(Crit) + battleLitanyAvg if hasDrg else 0 + chainStratAvg if hasSch else 0 + devilmentAvg if hasDnc else 0 + brdCritAvg if hasBrd else 0
    DHRate = CalcDHRate(DH) + (battleVoiceAvg+brdDhAvg) if hasBrd else 0 + devilmentAvg if hasDnc else 0
    CritDHRate = CritRate*DHRate
    NormalRate = 1-CritRate-DHRate+CritDHRate
    result = DamageSum * DamageSum * NormalRate + CritDamage * CritDamage * (CritRate-CritDHRate) + DHDamage * DHDamage * (DHRate-CritDHRate) + CritDHDamage * CritDHDamage * CritDHRate
    return result


def DamageMin(Potency, WD, JobMod, MainStat, Det, Crit, DH, SS, TEN, hasBrd, hasDrg, hasSch, hasDnc, classNum):
    MainStat = Math.floor(MainStat*(1+0.01*classNum))
    Damage = Math.floor(Potency*(WD+Math.floor(340*JobMod/1000))*(100+Math.floor((MainStat-340)*1000/2336))/100)
    Damage = Math.floor(Damage*(1000+Math.floor(130*(Det-340)/3300))/1000)
    Damage = Math.floor(Damage*(1000+Math.floor(100*(TEN-380)/3300))/1000)
    Damage = Math.floor(Damage*(1000+Math.floor(130*(SS-380)/3300))/1000/100)
    Damage = Math.floor(Damage*magicAndMend)
    Damage = Math.floor(Damage*enochian)

    return Math.floor(Damage*0.95)
