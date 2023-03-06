import pandas as pd
import numpy as np

PPSTable = pd.read_csv('Tables/PPSTable.csv')
np.save('data/PPSTable.npy', PPSTable.values)

MainStatValues = pd.read_csv('Tables/MainStatValues.csv', index_col=0).values
np.save('data/MainStatValues.npy', MainStatValues)

SecondaryMinorValues = pd.read_csv('Tables/SecondaryMinorValues.csv', index_col=0).values
np.save('data/SecondaryMinorValues.npy', SecondaryMinorValues)

SecondaryStatCapValues = pd.read_csv('Tables/SecondaryStatCapValues.csv', index_col=0).values
np.save('data/SecondaryStatCapValues.npy', SecondaryStatCapValues)

WDValues = pd.read_csv('Tables/WDValues.csv', index_col=0).values
np.save('data/WDValues.npy', WDValues)

GearType = pd.read_csv('Tables/GearType.csv')
GearType.to_pickle('data/GearType.pkl')

Menu = pd.read_csv('Tables/Menu.csv')
Menu.to_pickle('data/Menu.pkl')
