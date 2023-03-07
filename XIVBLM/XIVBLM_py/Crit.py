import numpy as np
def Crit_Rate(crit=400):
    return np.floor((200 * (crit - 400) / 1900 + 50)) / 1000

def Crit_Bonus(crit=400):
    return np.floor(200 * (crit - 400) / 1900 + 400) / 1000

def Crit_DPS(crit=400):
    return 1 + Crit_Rate(crit) * Crit_Rate(crit)
