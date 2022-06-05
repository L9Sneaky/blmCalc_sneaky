import torch
import tensorflow as tf
import pandas as pd
import numpy as np
import pickle
from itertools import product
# %%

x = pd.merge(pd.read_parquet('D:/data/X0.gzip'),pd.read_parquet('D:/data/X1.gzip'))
