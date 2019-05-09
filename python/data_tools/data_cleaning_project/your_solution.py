import example_solution
"""
Objective:

Normalize the "programming language" and "location" columns in data/messy.csv.
Output the results to data/out.csv. When the contents of data/out.csv are the
same as data/clean.csv you are finished.
"""

import os


# context manager
# with open(file_path, "r") as file_pointer:
#     for line in file_pointer:
#         if '"' in line:
#             print(line)


import numpy as np
import pandas as pd


def normalize_location(series):
    pass


def normalize_language(series):
    pass
    # return clean_series


def main():
    # load data
    df = pd.read_csv(os.path.join("..", "data", "messy.csv"))

    # clean location
    df["location"] = normalize_location(df["location"])
    # clean programming language
    df["programming language"] = normalize_language(df["programming language"])

    # output results
    df.to_csv(os.path.join("..", "data", "out.csv"), index=False)


if __name__ == "__main__":
    main()
