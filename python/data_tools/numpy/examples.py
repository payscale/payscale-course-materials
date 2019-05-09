import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# create 3 x 5 array of numbers from 0..14
print(np.arange(15))
arr = np.arange(15).reshape(3, 5)

print(arr)

# print(arr.shape)

# 2-dimensions
# print(arr.ndim)

# total number of elements
# print(arr.size)

# transpose
# print(arr.T)

# 1-d array
arr = np.array([1, 2, 3])
# print(arr)
# print(arr ** 2)
# print(2 * arr)
print(np.cumsum(arr))  # cumulative sum

# other array creation
# print(np.linspace(start=0, stop=100, num=25))
print(np.ones(25))
print(np.zeros(25))

# extract pandas column as numpy array using .values
df = pd.read_csv(os.path.join("..", "data", "clean.csv"))
arr = df["annual hours worked"].values
print(type(arr))
# print(arr)

# boolean slicing
# all the non-standard work hours
print(arr[arr != 2080])

# aggregations
# print(np.mean(arr))
# print(np.max(arr))
# print(np.min(arr))
# print(np.std(arr))

# generate data according to different statistical distributions
# we will learn more about matplotlib later

# exponential distribution
# plt.figure()
# scales = np.linspace(1, 3, 1000)
# arr = np.random.exponential(scale=scales)
# plt.hist(arr, bins=25)
# plt.show()

# binomial distribution
plt.figure()
arr = np.random.binomial(n=10, p=0.5, size=1000)
plt.hist(arr, bins=25)
plt.show()
