import numpy as np
from XIVBLM_py.DPS import DPS
from XIVBLM_py.GearStats import GearStats
from XIVBLM_py.GearIllegal import Gear_Illegal
def food_apply(materia_frame, gear_set, menu):
    if Gear_Illegal(materia_frame, gear_set):
        return {
            'Food': 'Illegal',
            'WD': 0,
            'Int': 0,
            'DH': 0,
            'Crit': 0,
            'Det': 0,
            'SS': 0,
            'DPS': 0
        }

    base_stats = GearStats(materia_frame, gear_set)
    menu['DPS'] = np.nan

    for i in range(len(menu)):
        menu['DH'][i] = min(np.floor(1.1 * base_stats['DH']), base_stats['DH'] + menu.iloc[i]['DH'])
        menu['Crit'][i] = min(np.floor(1.1 * base_stats['Crit']), base_stats['Crit'] + menu.iloc[i]['Crit'])
        menu['Det'][i] = min(np.floor(1.1 * base_stats['Det']), base_stats['Det'] + menu.iloc[i]['Det'])
        menu['SS'][i] = min(np.floor(1.1 * base_stats['SS']), base_stats['SS'] + menu.iloc[i]['SS'])
        menu['DPS'][i] = DPS(
            WD=base_stats['WD'],
            Int=base_stats['Int'],
            DH=menu.iloc[i]['DH'],
            Crit=menu.iloc[i]['Crit'],
            Det=menu.iloc[i]['Det'],
            SS=menu.iloc[i]['SS']
        )

    chef = menu['DPS'].idxmax()
    return {
        'Food': menu.loc[chef, 'Food'],
        'WD': base_stats['WD'],
        'Int': base_stats['Int'],
        'DH': menu.loc[chef, 'DH'],
        'Crit': menu.loc[chef, 'Crit'],
        'Det': menu.loc[chef, 'Det'],
        'SS': menu.loc[chef, 'SS'],
        'DPS': menu.loc[chef, 'DPS']
    }
