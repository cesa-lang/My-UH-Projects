import numpy as np

data = [12,10,15,8,80,13]

mean, std_dev = np.mean(data),np.std(data)

threshold = mean + 2 * std_dev
anomalies = [x for x in data if x > threshold]

print(data)
print(anomalies)