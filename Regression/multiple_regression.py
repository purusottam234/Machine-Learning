import pandas
from sklearn import linear_model

df = pandas.read_csv('/home/purusottam/Downloads/data.csv')
x = df[['Weight','Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(x,y)
# predict the CO2 emmission of a car where weight is 2300kg and volume is 1000cm3
predictedco2 = regr.predict([[2300,1000]])
print(predictedco2)


# Coefficient
# Coefficient is a factor that describes the relationship with an unknown variable
# eg if x is a variable, then 2x is x two times.x is unknown variable, and the number 2 is the coefficient
print(regr.coef_)
# Weight:0.00755095
# Volume:0.007805261
# This tells us tht if weight is increased by 1 kg, co2 emission increases by 0.00755095g


# We can test by increasing weight