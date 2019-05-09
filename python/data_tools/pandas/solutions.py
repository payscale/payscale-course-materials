import os

import pandas as pd


df = pd.read_csv(os.path.join("..", "data", "clean.csv"))
annual_hour_ratio = df["annual hours worked"] / 2080
df["normalized salary"] = df["annual salary"] / annual_hour_ratio
print(df.head())

# which city has the most haskell programmers?
print("Exercise 1:")
solution = df[df["programming language"] == "haskell"] \
    [["location", "normalized salary"]] \
    .groupby("location") \
    .count() \
    .rename(columns={"normalized salary": "count"}) \
    .sort_values(by="count", ascending=False)
# NOTE: the .rename() and .sort_values() aren't necessary
print(solution)

# where does the highest normalized salary programmer live?
print("Exercise 2:")
solution = df.sort_values(by="normalized salary", ascending=False)["location"].head(1)
print(solution)

# what language do they use?
print("Exercise 3:")
solution = df \
    .sort_values(by="normalized salary", ascending=False) \
    ["programming language"] \
    .head(1)
print(solution)

# what is the average salary by programming language?
print("Exercise 4:")
solution = df[["programming language", "normalized salary"]] \
    .groupby("programming language") \
    .mean()
print(solution)

# where do programmers work the longest hours?
print("Exercise 5:")
solution = df \
    [["location", "annual hours worked"]] \
    .groupby("location") \
    .mean() \
    .sort_values("annual hours worked", ascending=False) \
    .rename(columns={"annual hours worked": "mean annual hours worked"})
print(solution)
