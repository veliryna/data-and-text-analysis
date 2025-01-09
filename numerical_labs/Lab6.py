import pandas as pd
import numpy as np

data = pd.read_excel('PythonLabs/Version 4.xlsx')
print(data)

data.rename(columns = {'species':'Species', 'island':'Island', 'culmen_length_mm':'Culmen_Length', 'culmen_depth_mm':'Culmen_Depth', 'flipper_length_mm':'Flipper_Length', 'body_mass_g':'Body_Mass', 'sex':'Sex'}, inplace = True)
data.drop('Unnamed: 0', inplace=True, axis=1)
print(data)

print(data.describe())
print()
print(data.info())
print()

data=data.assign(Culmen_Length=lambda x: x.Culmen_Length.replace(599990.9, np.nan),
Flipper_Length=lambda x: x.Flipper_Length.replace(-218.0, np.nan),
Culmen_Depth=lambda x: x.Culmen_Depth.replace(3314.6, np.nan))

data=data.assign(Culmen_Length=lambda x : x.Culmen_Length.fillna(method='ffill'),
Flipper_Length=lambda x : x.Flipper_Length.fillna(method='ffill'),
Culmen_Depth=lambda x : x.Culmen_Depth.fillna(method='ffill'),
Body_Mass=lambda x : x.Body_Mass.fillna(method='ffill'),
Sex=lambda x : x.Sex.fillna(method='ffill'))

data['Species'] = data['Species'].str.title()
data['Island'] = data['Island'].str.title()
data['Sex'] = data['Sex'].str.title()

print("Unique string values: ")
print(data['Species'].unique())
print(data['Island'].unique())
print(data['Sex'].unique())
print()

data['Species'] = data['Species'].replace('Adelie&', 'Adelie')
data['Island'] = data['Island'].replace('B???', 'Biscoe')
data['Sex'] = data['Sex'].replace(['Error', 'Boy'],'Male')
data['Sex'] = data['Sex'].replace('Girl','Female')

print("After renaming values with mistakes: ")
print(data['Species'].unique())
print(data['Island'].unique())
print(data['Sex'].unique())
print()

data.drop_duplicates(inplace=True)
data.sort_values(by = ['Species', 'Island'], inplace=True)
data.reset_index(drop=True, inplace=True)

print(data)

data.to_excel('PythonLabs/penguins.xlsx')