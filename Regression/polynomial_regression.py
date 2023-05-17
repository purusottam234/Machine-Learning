# Polynomial Regression

'''
If your data points clearly will not fit a linear Regression,it might be ideal for polynomial regression

'''
import numpy as np
import matplotlib.pyplot as plt
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# plt.scatter(x, y)
# plt.show()

# numpy method to make polynomial model
mymodel = np.poly1d(np.polyfit(x,y,3))
# specify how line will display,we start at position 1 and end at position 22
myline = np.linspace(1,22,100)
plt.scatter(x,y)
# Draw the line of polynomial regression
plt.plot(myline,mymodel(myline))
plt.show()


# R Squared
# If there is no relationship the polynomial regression can not be used to predict anything
# the relationship is measured with a value called the r-squared
# The r-squared value ranges from 0 to 1 where 0 means no relationship and 1 means 100% related
from sklearn.metrics import r2_score

print(r2_score(y,mymodel(x)))

# Predict the future 
# Predict the speed of a car passing at 17:00
speed=mymodel(17)
print(speed)