import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


DATA_DIR = os.path.join("..", "data")
PLOT_DIR = "plots"

prog_lang_col = "programming language"
annual_hrs_worked_col = "annual hours worked"
annual_salary_col = "annual salary"
norm_salary_col = "normalized salary"
location_col = "location"

df = pd.read_csv(os.path.join(DATA_DIR, "clean.csv"))
annual_hour_ratio = df[annual_hrs_worked_col] / 2080
df[norm_salary_col] = df[annual_salary_col] / annual_hour_ratio

python_salaries = df[df[prog_lang_col] == "python"][norm_salary_col].values
haskell_salaries = df[df[prog_lang_col] == "haskell"][norm_salary_col].values
c_sharp_salaries = df[df[prog_lang_col] == "c#"][norm_salary_col].values
java_salaries = df[df[prog_lang_col] == "java"][norm_salary_col].values

seattle_salaries = df[df[location_col] == "Seattle"][norm_salary_col].values
denver_salaries = df[df[location_col] == "Denver"][norm_salary_col].values
cary_salaries = df[df[location_col] == "Cary"][norm_salary_col].values
louisville_salaries = df[df[location_col] == "Louisville"][norm_salary_col].values

### bar plot of average salary by language
xs = ["Python", "Haskell", "C#", "Java"]
ys = [
    np.mean(python_salaries),
    np.mean(haskell_salaries),
    np.mean(c_sharp_salaries),
    np.mean(java_salaries),
]

# plt.figure()
# plt.bar(xs, ys)
# plt.savefig(os.path.join(PLOT_DIR, "bar.png"))

### bar plot with title, xlabel, ylabel
xs = ["Python", "Haskell", "C#", "Java"]
ys = [
    np.mean(python_salaries),
    np.mean(haskell_salaries),
    np.mean(c_sharp_salaries),
    np.mean(java_salaries),
]

# plt.figure()
# ax = plt.gca()
# ax.tick_params(axis='both', which='major', labelsize=6)
# plt.bar(xs, ys)
# plt.xlabel("Programming Language")
# plt.ylabel("Normalized Salary")
# plt.title("Programming Language Salaries")
# plt.savefig(os.path.join(PLOT_DIR, "bar_w_labels.png"))

### line plot of number of programmers by location
# xs = ["Denver", "Seattle", "Cary", "Louisville"]
# ys = [
#     len(denver_salaries),
#     len(seattle_salaries),
#     len(cary_salaries),
#     len(louisville_salaries),
# ]

# plt.figure()
# plt.plot(xs, ys)
# plt.savefig(os.path.join(PLOT_DIR, "line.png"))

### scatter plot of number of programmers by location
xs = ["Denver", "Seattle", "Cary", "Louisville"]
ys = [
    len(denver_salaries),
    len(seattle_salaries),
    len(cary_salaries),
    len(louisville_salaries),
]

plt.figure()
plt.scatter(xs, ys)
plt.show()
# plt.savefig(os.path.join(PLOT_DIR, "scatter.png"))

### scatter plot and line plot together using different colors and setting y-axis limits
# xs = ["Denver", "Seattle", "Cary", "Louisville"]
# ys = [
#     len(denver_salaries),
#     len(seattle_salaries),
#     len(cary_salaries),
#     len(louisville_salaries),
# ]

# plt.figure()
# plt.plot(xs, ys, color="c", linestyle="--")  # cyan dashed
# plt.scatter(xs, ys, s=80, facecolors='none', edgecolors='r')  # hollow red circles
# plt.ylim([0, max(ys) + 1])
# plt.savefig(os.path.join(PLOT_DIR, "dot_and_line.png"))

### box and whisker plot of programming language salaries
# plt.figure()
# plt.boxplot(python_salaries)
# plt.savefig(os.path.join(PLOT_DIR, "boxplot.png"))

### overlapping histograms with opacity
# experiment with differnt styles
# plt.style.use("dark_background")
# plt.style.use("ggplot")
# plt.style.use("fivethirtyeight")
# plt.style.use('bmh')

# randomly generated data
# x = np.random.normal(loc=-5, scale=1, size=150)
# y = np.random.normal(loc=0, scale=2, size=150)
# z = np.random.normal(loc=5, scale=3, size=150)

# plt.figure()
# ax = plt.gca()
# ax.hist(x, alpha=0.5)
# ax.hist(y, alpha=0.5)
# ax.hist(z, alpha=0.5)
# plt.savefig(os.path.join(PLOT_DIR, "histograms.png"))
