# Varience indicates how spread out the values are
# square root of varience is SD
# Square of SD is varience

import numpy as np

data = [99,86,87,88,111,86,103,87,94,78,77,85,86,33,44,55,12,34,56]

x = np.var(data)

print(x)