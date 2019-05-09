import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(os.path.join("..", "data", "clean.csv"))
annual_hour_ratio = df["annual hours worked"] / 2080
df["normalized salary"] = df["annual salary"] / annual_hour_ratio
cities = df["location"].values
salaries = df["normalized salary"].values

# how many programmers make more than 200K?
# hint: boolean slicing
total = len(salaries)
over_200k = len(salaries[salaries > 200000])
print(f"{over_200k} out of {total} make over 200K")

# which city has the highest standard deviation for salaries?
# hint: first slice by city
max_std = np.std(salaries[cities == "Seattle"])
associated_city = "Seattle"
for city in ["Cary", "Denver", "Louisville"]:
    city_std = np.std(salaries[cities == city])
    if city_std > max_std:
        max_std = city_std
        associated_city = city
print(f"{associated_city} has the highest standard devation of salaries at: {max_std}")

# for the following two problems, use this documentation:
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html#numpy.random.normal
# and refer to the plotting examples in examples.py

# create and plot a random normal distrition centered at 0 with
# a standard deviation of 2.5
plt.figure()
arr = np.random.normal(loc=0, scale=2.5, size=1000)
plt.hist(arr, bins=25)
plt.show()

# create and plot a random normal distrition centered at 10 with
# a standard deviation of 5
plt.figure()
arr = np.random.normal(loc=10, scale=5, size=1000)
plt.hist(arr, bins=25)
plt.show()
