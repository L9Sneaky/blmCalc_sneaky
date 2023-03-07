import numpy as np

def FoodFrame(Menu, minIlvl):
    Food = Menu[Menu['Ilvl'] >= minIlvl].copy()
    Food['Remove'] = np.nan
    Food = Food.reset_index(drop=True)
    for i in range(len(Food)):
        cond1 = Food['DH'] >= Food.loc[i, 'DH']
        cond2 = Food['Crit'] >= Food.loc[i, 'Crit']
        cond3 = Food['Det'] >= Food.loc[i, 'Det']
        cond4 = Food['SS'] >= Food.loc[i, 'SS']
        
        intersect_1 = np.intersect1d(np.where(cond1)[0], np.where(cond2)[0])
        intersect_2 = np.intersect1d(np.where(cond3)[0], np.where(cond4)[0])
        
        Food.loc[i, 'Remove'] = len(np.intersect1d(intersect_1, intersect_2)) - 1
    
    Food = Food[Food['Remove'] < 1].reset_index(drop=True)
    Food.drop('Remove', axis=1, inplace=True)
    
    return Food.reset_index(drop=True)
