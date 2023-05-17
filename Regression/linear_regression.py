# Regression : used to find the relationship between variables
# In Machine learning that relationship is used to predict the outcomes 
# of future events

# Linear Regression: uses the relationship between the data points to
# draw a straight line through all them. this line can be used to predict future values


import matplotlib.pyplot as plt
from scipy import stats

# x = [4,3,5,1,6,8,12,14,21,32,45,65,12,33,78,99]
# y = [99,12,41,23,45,67,78,90,21,32,54,56,78,89,67,45]
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# plt.scatter(x,y)
# plt.show()

slope, intercept, r, p,std_err = stats.linregress(x,y)

# create a function that uses the slope and intercept values to return
# a new value. The new value represents where on the y axis the corresponding x value will be placed

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc,x)) #run each value of x array through the function and this will result in a new array with new values for y axis
plt.scatter(x,y) #Draw original scatter plot
plt.plot(x,mymodel) #It will draw the line of linear regression
plt.show() #display diagram


# R for Relationship
"""
It is important to know the relationship between the values of x-axis and values of y-axis, If 
there is no relationship the linear regression can not be used to predict anything
This relationship the coefficient of correlation is called r
The r value ranges from -1 to 1 where 0 means no relationship and 1(and -1) means 100% related
Python and Scipy module will compute this value for us, all we have to do is feed 
it with x and y values
"""
print(r) #result -0.76 shows that there is relationship, not perfect but it indicates we could use linear regression in future predictions


# Lets predict the speed of a 10 years old car
speed = myfunc(10)
print(speed)