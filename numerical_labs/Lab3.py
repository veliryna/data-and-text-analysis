import pandas as pd
import numpy as np
data = pd.read_csv('frogs.csv')
col1 = pd.Series(data['NoOfPools'])
a = col1[4:8]
index = ['I', 'II', 'III', 'IV']
a.index = index
print(a)
print()
print(data.iloc[:4, :4])
print()
print(data.loc[:5,:'altitude'])

data['ratioAD'] = data['altitude']/(data['distance']) #add column
print(data)
newrow = pd.DataFrame([[121, 1098, 1666, 2380]],columns=['northing', 'easting', 'altitude','distance'])
data = pd.concat([data, newrow]) #add row
print(data)
data.drop(1) #delete row
del data['Unnamed: 0'] #delete column
print(data)

data = data.set_index(['NoOfSites'])
print(data)
print(data.describe())
print(data.dtypes)
data['easting'] = data['easting'].astype('float64')
print(data.dtypes)
print(data.groupby('pres.abs').mean())
print(data.groupby('pres.abs').agg({'avrain': max,'NoOfPools': np.median}))
print(data[(data.distance>600)&(data.distance<1000)]) #subarray

'''New DataFrame'''
body_length = np.random.randint(7, 15,size=(30))
body_weight = np.random.randint(50, 100, size=(30))
gend_dist = np.random.randint(0, 2, size=(30))
frogs = pd.DataFrame({'Length':body_length, 'Weight':body_weight})
gender = pd.DataFrame({'Gender':gend_dist})
print(frogs)
frogs = pd.concat([frogs, gender], axis=1)
print(frogs)
df2 = pd.DataFrame({'Length':np.random.randint(5, 13,size=(30)), 'NoOfPools': np.random.randint(100, 200,size=(30))})
print(pd.merge(frogs, df2, on='Length')) 