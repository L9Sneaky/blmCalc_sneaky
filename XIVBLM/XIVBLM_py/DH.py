import numpy as np

def DHRate(DirectHit=400):
    return np.floor(550*(DirectHit-400)/1900)/1000

def DH_DPS(DirectHit=400):
    return 1+DHRate(DirectHit)/4