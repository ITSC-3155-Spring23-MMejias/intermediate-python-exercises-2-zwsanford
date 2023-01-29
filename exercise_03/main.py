import numpy as np

sample_list = np.random.uniform(low = 0, high = 1, size = 10)
mean = np.mean(sample_list)
median = np.median(sample_list)
std = np.std(sample_list)

print(sample_list)
print("Mean: " + str(mean))
print("Median: " + str(median))
print("Standard Deviation: " + str(std))