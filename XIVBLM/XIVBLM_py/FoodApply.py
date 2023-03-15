import numpy as np
# from XIVBLM_py.DPS import DPS
from XIVBLM_py.dpsCalc import DPS
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
    copy_menu = menu.copy()
    copy_menu['DPS'] = np.nan

    for i in range(len(menu)):
        copy_menu['DH'][i] = min(np.floor(1.1 * base_stats['DH']), base_stats['DH'] + menu.iloc[i]['DH'])
        copy_menu['Crit'][i] = min(np.floor(1.1 * base_stats['Crit']), base_stats['Crit'] + menu.iloc[i]['Crit'])
        copy_menu['Det'][i] = min(np.floor(1.1 * base_stats['Det']), base_stats['Det'] + menu.iloc[i]['Det'])
        copy_menu['SS'][i] = min(np.floor(1.1 * base_stats['SS']), base_stats['SS'] + menu.iloc[i]['SS'])
        copy_menu['DPS'][i] = DPS(
            WD=base_stats['WD'],
            Int=base_stats['Int'],
            DH=copy_menu.iloc[i]['DH'],
            Crit=copy_menu.iloc[i]['Crit'],
            Det=copy_menu.iloc[i]['Det'],
            SS=copy_menu.iloc[i]['SS']
        )

    chef = copy_menu['DPS'].idxmax()
    return {
        'Food': copy_menu.loc[chef, 'Food'],
        'WD': base_stats['WD'],
        'Int': base_stats['Int'],
        'DH': copy_menu.loc[chef, 'DH'],
        'Crit': copy_menu.loc[chef, 'Crit'],
        'Det': copy_menu.loc[chef, 'Det'],
        'SS': copy_menu.loc[chef, 'SS'],
        'DPS': copy_menu.loc[chef, 'DPS']
    }
