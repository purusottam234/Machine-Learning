# Tran and Test
'''
Train/Test is a method to measure the accuracy of your model
It is called Train/Test because you split the data set into two sets: a training and testing set
Train the model means create the model
Test the model means test the accuracy of model
'''

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3,1,100)
y = numpy.random.normal(150,40,100)/x
# plt.scatter(x,y)
# plt.show()

train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x,train_y,4))
myline = numpy.linspace(0,6,100)
plt.scatter(train_x,train_y)
plt.plot(myline,mymodel(myline))
plt.show()

from sklearn.metrics import r2_score

r2 = r2_score(train_y,mymodel(train_x))
print(r2)

# plt.scatter(train_x,train_y)
# plt.show()
r_2 = r2_score(test_y,mymodel(test_x))
print(r_2)

# Predict the value
print(mymodel(5))