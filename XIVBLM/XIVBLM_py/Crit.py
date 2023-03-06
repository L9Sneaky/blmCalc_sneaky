import numpy as np
def crit_rate(crit=400):
    return np.floor((200 * (crit - 400) / 1900 + 50)) / 1000

def crit_bonus(crit=400):
    return np.floor(200 * (crit - 400) / 1900 + 400) / 1000

def crit_dps(crit=400):
    return 1 + crit_rate(crit) * crit_bonus(crit)
