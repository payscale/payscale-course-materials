"""Examples of using clustering algorithms on network traffic data."""

import numpy as np
import sklearn
import matplotlib.pyplot as plt
from sklearn import cluster, mixture
from scipy import stats


plt.style.use('ggplot')


# simulate hourly network traffic data over 2 weeks
# wher etraffic is higher during busy hours
hours = range(1, 25)  # 1-24
days = range(1, 8)  # 1-7
weeks = range(1, 2)  # 1
total_hours = range(1, (len(hours) * len(days) * len(weeks)) + 1)

usage = []
for week in weeks:
    for day in days:
        for hour in hours:
            if 8 < hour < 16:
                # get a large random number from a normal distribution
                # during work hours
                usage_this_hour = np.random.normal(loc=800, scale=200)
            else:
                # get a small random number from an exponential distrbution
                usage_this_hour = np.random.exponential(scale=50)
            usage.append(usage_this_hour)
            
usage = np.array(usage)
total_hours = np.array(total_hours)

print(usage)

# line plot
# plt.figure()
# plt.plot(total_hours, usage, "b-.")
# plt.show()

# histogram showing the two different distributions
# plt.figure()
# plt.hist(usage, bins=20)
# plt.show()

# k-means clustering

# need to create a 2-d matrix
usage_mat = []
for h, u in zip(total_hours, usage):
    usage_mat.append([h, u])
usage_mat = np.array(usage_mat)

# print(usage_mat)

k_means = cluster.KMeans(n_clusters=2)
k_means.fit(usage_mat)

# view the assigned clusters
print(k_means.labels_)

# using numpy boolean slicing/masking to get usage and hours for the given clusters
high_usage = usage[k_means.labels_ == 1]
high_hours = total_hours[k_means.labels_ == 1]
low_usage = usage[k_means.labels_ == 0]
low_hours = total_hours[k_means.labels_ == 0]

# plt.figure()
# plt.plot(high_hours, high_usage, 'go')
# plt.plot(low_hours, low_usage, 'ro')
# plt.show()

# using scipy.stats.linregress to do a linear regression through just the busy hours
# slope, intercept = stats.linregress(high_hours, high_usage)[:2]
# plt.figure()
# plt.plot(total_hours, usage, 'bo')
# plt.plot(high_hours, intercept + slope*high_hours, 'g-', linewidth=2)
# plt.show()

# compare a linear regression through all the points and one that just goes
# through the busy cluster, and one that just goes through the non-busy cluster
# upper_avg = np.repeat(a=np.mean(high_usage), repeats=len(high_usage))
# lower_avg = np.repeat(a=np.mean(low_usage), repeats=len(low_usage))
# total_avg = np.repeat(a=np.mean(usage), repeats=len(usage))
# plt.figure()
# plt.plot(total_hours, usage, 'bo')
# plt.plot(total_hours, total_avg, 'm-', linewidth=2)
# plt.plot(high_hours, upper_avg, 'y-', linewidth=2)
# plt.plot(low_hours, lower_avg, 'g-', linewidth=2)
# plt.show()


# Gaussian Mixed Model
g = mixture.GMM(n_components=2)
g.fit(usage.reshape(len(usage), 1))
print(usage)
print(usage.reshape(len(usage), 1))

# view the means of the underlying estimated distributions
print(g.means_)

# predict which points should belong to each distribution
# Expectation-Maximization algorithm
predictions = g.predict(usage.reshape(len(usage), 1))
g.predict(usage.reshape(len(usage), 1))

# plot clusters like we did with k-means
high_usage = usage[predictions == 1]
high_hours = total_hours[predictions == 1]
low_usage = usage[predictions == 0]
low_hours = total_hours[predictions == 0]

plt.figure()
plt.plot(high_hours, high_usage, 'go')
plt.plot(low_hours, low_usage, 'ro')
plt.show()
