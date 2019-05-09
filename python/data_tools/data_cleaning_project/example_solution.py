"""
Objective:

Normalize the "programming language" and "location" columns in data/messy.csv.
Output the results to data/out.csv. When the contents of data/out.csv are the
same as data/clean.csv you are finished.
"""

import os

import numpy as np
import pandas as pd


def normalize_location(raw_locations):
    normalized_values = []
    for location in raw_locations:
        location = location.split(",")[0]
        location = location.title()
        normalized_values.append(location)
    return normalized_values


def normalize_programming_language(raw_prog_langs):
    normalized_prog_langs = []
    for prog_lang in raw_prog_langs:
        the = "The "
        if the in prog_lang:
            prog_lang = prog_lang.split(the)[1]
        prog_lang = prog_lang.split(" Programming Language")[0]
        prog_lang = prog_lang.lower()
        normalized_prog_langs.append(prog_lang)
    return normalized_prog_langs


df = pd.read_csv(os.path.join("..", "data", "messy.csv"))

df["location"] = normalize_location(df["location"])
df["programming language"] = normalize_programming_language(df["programming language"])

# for col in df.columns:
#     if col != "annual salary":
#         print()
#         print(col)
#         print(df[col].drop_duplicates())

df.to_csv(os.path.join("..", "data", "out.csv"), index=False)
