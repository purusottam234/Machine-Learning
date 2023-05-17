# Scale Features
'''
When our data has different values, and even different measurement units, it can be difficult to compare them.
What is kilograms compared to meters? or altitude compared with Time?
The solution is Scaling.We can scale data into new values that are easier to compare
There are different methods for scaling Data but we will use a method called Standardization
Standardization method uses this formula:
z = (x-u)/s
where z is the new value, x is original value, u is the mean and s is the standard deviation
Python sklearn module has a method called StandardScaler() which return a Scaler object with
methods for transforming data sets
'''

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("/home/purusottam/Downloads/data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)
print(scaledX)


# Predict CO2 values
# When the data set is scaled, you will have to use the scale when you predict values

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)