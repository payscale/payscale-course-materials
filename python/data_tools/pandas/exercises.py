import os

import pandas as pd


df = pd.read_csv(os.path.join("..", "data", "clean.csv"))
annual_hour_ratio = df["annual hours worked"] / 2080
df["normalized salary"] = df["annual salary"] / annual_hour_ratio
print(df.head())

# which city has the most haskell programmers?
# hint: df.groupby("column_name").count()  might be useful
print("Exercise 1:")
# df = df[df["programming language"] == "haskell"] \
#     [["location", "programming language"]] \
#     .groupby("location") \
#     .count() \
#     .sort_values(by="programming language", ascending=False)
# print(df)
solution = df[df["programming language"] == "haskell"] \
    [["location", "programming language"]] \
    .groupby("location") \
    .count() \
    .rename(columns={"programming language": "count"}) \
    .sort_values(by="count", ascending=False)
print(solution)

# where does the highest salaried programmer live?
print("Exercise 2:")
solution = df.sort_values(by="normalized salary", ascending=False).head(1)
print(solution)

# what language do they use?
print("Exercise 3:")
solution = df.sort_values(by="normalized salary", ascending=False).head(1)
print(solution)

# what is the average salary by programming language?
print("Exercise 4:")

# where do programmers work the longest hours?
print("Exercise 5:")
