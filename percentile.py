# Percentile are used in statistics to give you a number that describes
# the value that a given percent of the values are lower than


import numpy as np

data = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31,22,34,12,24]
x = np.percentile(data,45)
print(x)

y = np.percentile(data,75)

print(y)