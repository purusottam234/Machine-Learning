import sys
import matplotlib
matplotlib.use('Agg')
import pandas

df = pandas.read_csv('/home/purusottam/Downloads/data_set.csv')
print(df)

# We have to convert the non numerical colums into numerical values
d = {'UK':0,'USA':1,"N":3}
df['Nationality']  = df['Nationality'].map(d)
d = {'YES':1,'NO':0}
df['Go'] = df['Go'].map(d)
print(df)
# Seperate features columns from target column

features = ['Age','Experience','Rank','Nationality']
x = df[features]
y=df['Go']
print(x)
print(y)

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
dtree = DecisionTreeClassifier()
dtree = dtree.fit(x,y)
tree.plot_tree(dtree,feature_names=features)


plt.savefig('tree.png')


 
# Image(filename='tree.png')

 
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()