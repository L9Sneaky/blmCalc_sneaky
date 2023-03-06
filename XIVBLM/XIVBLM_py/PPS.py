import numpy as np
import pandas as pd

PPSTable = pd.read_csv('Tables/PPSTable.csv')

def PPS(SS=400, Crit=400):
    Tier = np.argmax(PPSTable["SpS"] > SS) - 1
    return PPSTable["PPS"][Tier]
