# SD is a number that describes how spread out the values are
# A low SD means that most of the numbers are close to the mean value
# A high SD means that the values are spread out over a wider range


import numpy as np

data = [99,86,87,88,111,86,103,87,94,78,77,85,86,99,33,45]

x = np.std(data)
print(x)