import os

import pandas as pd


df = pd.read_csv(os.path.join("..", "data", "clean.csv"))
annual_hour_ratio = df["annual hours worked"] / 2080
df["normalized salary"] = df["annual salary"] / annual_hour_ratio
print(df.head())

# which city has the most haskell programmers?
# hint: df.groupby("column_name").count()  might be useful
print("Exercise 1:")

# where does the highest salaried programmer live?
print("Exercise 2:")

# what language do they use?
print("Exercise 3:")

# what is the average salary by programming language?
print("Exercise 4:")

# where do programmers work the longest hours?
print("Exercise 5:")
