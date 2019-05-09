"""
create a 2-d scatter plot where
the x-label is programming language
the y-label is city
and the size of the points are proportional to the number of programmers

hints:
- a nested loop might be useful
- need to filter the dataframe based on location and language, then compute length
- see the "hollow red circles" scatter plot in examples.py
- may need to fiddle with scaling factor for circle size
- effectively this plot is a pivot table
"""

import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


DATA_DIR = os.path.join("..", "data")
PLOT_DIR = "plots"

prog_lang_col = "programming language"
location_col = "location"

df = pd.read_csv(os.path.join(DATA_DIR, "clean.csv"))

# insert solution here:
