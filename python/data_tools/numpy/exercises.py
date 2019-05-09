import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(os.path.join("..", "data", "clean.csv"))
annual_hour_ratio = df["annual hours worked"] / 2080
df["normalized salary"] = df["annual salary"] / annual_hour_ratio
cities = df["location"].values
salaries = df["normalized salary"].values

print(cities)
print(np.unique(cities))
print(salaries)

print()
print("")
print()

# how many programmers make more than 200K?
# hint: boolean slicing
print(salaries[salaries > 200000])

# which city has the largest standard deviation for salaries?
# hint: first slice by city
max_std = -1
max_city = ""
for city in np.unique(cities):
    new_std = np.std(salaries[cities == city])
    if new_std > max_std:
        max_std = new_std
        max_city = city
print(max_city)
print(max_std)


# for the following two problems, use this documentation:
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html#numpy.random.normal
# and refer to the plotting examples in examples.py

# create and plot a random normal distrition centered at 0 with
# a standard deviation of 2.5

# create and plot a random normal distrition centered at 10 with
# a standard deviation of 5
