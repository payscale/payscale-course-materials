"""
create a 2-d scatter plot where
the x-label is programming language
the y-label is city
and the size of the points are proportional to the number of programmers

hints:
- a nested loop might be useful
- need to filter the dataframe based on location and language, then compute length
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
xs = ["python", "haskell", "c#", "java"]
ys = ["Denver", "Seattle", "Cary", "Louisville"]

plt.style.use("ggplot")
plt.figure()
for x in xs:
    for y in ys:
        number_of_programmers = len(df[(df[prog_lang_col] == x) & (df[location_col] == y)])
        size = number_of_programmers * 200
        plt.scatter(x, y, s=size, facecolors='none', edgecolors='r')
plt.savefig(os.path.join(PLOT_DIR, "variable_circles.png"))
