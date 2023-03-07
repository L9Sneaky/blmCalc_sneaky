import numpy as np
from XIVBLM_py.DH import DH_DPS
from XIVBLM_py.Crit import Crit_DPS
from XIVBLM_py.Det import Det_DPS
from XIVBLM_py.PPS import PPS
from XIVBLM_py.DamagePerPotency import damage_per_potency

def DPS(WD, Int, DH, Crit, Det, SS):
    SelfEsteem = np.floor(100 * PPS(SS) * damage_per_potency(WD, np.floor(Int * 1.05)))
    SelfEsteem = np.floor(SelfEsteem * Det_DPS(Det) / 100)
    SelfEsteem = np.floor(1.3 * SelfEsteem)
    SelfEsteem = np.floor(1.2 * SelfEsteem)
    return SelfEsteem * DH_DPS(DH) * Crit_DPS(Crit)