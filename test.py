import pandas as pd
import numpy as np
from math import floor
# %%
lvlmain = 390
lvldiv = 1900
INT = 2571
# f(DET) = ⌊ 140 × ( DET - Level Lv, MAIN )/ Level Lv, DIV + 1000 ⌋
def det_Mult(det = 0):
    return floor(140*(det - lvlmain)/lvldiv+1000)/1000

arr = np.asarray(range(390,2691))

det_arr = []
for i in arr:
    det_arr.append(det_Mult(i))
det_arr = np.asarray(det_arr)


pd.DataFrame(np.asarray([arr, det_arr]).T, columns = ['det', 'multiplyer']).plot()
