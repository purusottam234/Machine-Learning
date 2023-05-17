import numpy as np
from scipy import stats

data  = [99,34,55,23,55,67,87,99,12,55,34,65,99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(data)
print(x)
