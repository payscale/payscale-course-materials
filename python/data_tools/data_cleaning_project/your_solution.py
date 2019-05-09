"""
Objective:

Normalize the "programming language" and "location" columns in data/messy.csv.
Output the results to data/out.csv. When the contents of data/out.csv are the
same as data/clean.csv you are finished.
"""

import os

import numpy as np
import pandas as pd


df = pd.read_csv(os.path.join("..", "data", "messy.csv"))

# insert solution here that normalizes the columns in `df`

df.to_csv(os.path.join("..", "data", "out.csv"), index=False)

