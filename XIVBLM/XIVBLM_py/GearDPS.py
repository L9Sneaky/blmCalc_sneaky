import numpy as np
from XIVBLM_py.GearStats import GearStats
from XIVBLM_py.Gear_Illegal import Gear_Illegal
def GearDPS(MateriaFrame, GearSet):
    Stats = GearStats(MateriaFrame, GearSet)
    if Gear_Illegal(MateriaFrame, GearSet):
        return 0
    return DPS(WD=Stats['WD'],
               Int=Stats['Int'],
               DH=Stats['DH'],
               Crit=Stats['Crit'],
               Det=Stats['Det'],
               SS=Stats['SS'])
