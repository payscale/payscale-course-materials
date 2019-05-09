import os

import pandas as pd


# read in csv file
df = pd.read_csv(os.path.join("..", "data", "clean.csv"))

# display the first 5 rows of a dataframe
# print(df.head())

# display the last 5 rows of a dataframe
# print(df.tail())

# display the first n rows of a dataframe (n=10 in this case)
# print(df.head(10))

# perform division on a column
# this computes the amount everyone would make if they worked 40 hrs a week,
# 52 days a year
annual_hour_ratio = df["annual hours worked"] / 2080
# print(annual_hour_ratio)
df["normalized salary"] = df["annual salary"] / annual_hour_ratio
# print(df.head())

# make a new dataframe, only keeping two columns from the original
prog_lang_df = df[["programming language", "normalized salary"]]
# print(prog_lang_df.head())

# compute the mean salary by programming language
mean_lang_df = prog_lang_df.groupby("programming language").mean()
# print(mean_lang_df)

# compute the peak salary by programming language
max_lang_df = prog_lang_df.groupby("programming language").max()
# print(max_lang_df)

# filter a dataframe by column value
python_df = df[df["programming language"] == "python"]
# print(python_df)

# filter a dataframe by two column values
# df[(condition) | (condition)]
denver_class_df = df[
    (df["programming language"] == "python") & (df["location"] == "Denver")
]
# print(denver_class_df)

# create a pivot table where
# - the column index is programming language
# - the row index is location
# - the pivot value is the number of programmers
df["index"] = "dummy index"
pivot_df = pd.pivot_table(
    df,
    columns=["programming language", "location"],
    index="index",
    values="normalized salary",
    aggfunc="count",
)
pivot_df = pivot_df.reindex_axis(some_index, axis=1)
pivot_df = pivot_df.fillna(0)
pivot_df.to_excel("pivot.xlsx")
exit()
# print(pivot_df.fillna(0))  # fill np.nan (not a number) values

# read in an excel sheet
sheet1_df = pd.read_excel(os.path.join("..", "data", "test.xlsx"), sheet_name="Sheet1")
print("the first sheet")
print(sheet1_df.head())
sheet2_df = pd.read_excel(os.path.join("..", "data", "test.xlsx"), sheet_name="Sheet2")
print("the second sheet")
print(sheet2_df.head())

# list the sheet names in an excel file
excel_file = pd.ExcelFile(os.path.join("..", "data", "test.xlsx"))
print(excel_file.sheet_names)

# df = df.set_index(["location", "programming language"])

# write dataframe back out to excel
df.to_excel("out.xlsx", sheet_name="Output")
# can also write to csv with df.to_csv()

# sort dataframe by column
# sorted_df = df.sort_values(by="normalized salary", ascending=False)
# print(sorted_df.head())
