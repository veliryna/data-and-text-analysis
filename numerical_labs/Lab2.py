import pandas as pd
import scipy.stats 

data = pd.read_csv('frogs.csv')
avg = data.groupby('pres.abs').mean()

print("Average distance where frogs are present: ", avg.at[0, 'distance'])
print("Average distance where frogs are NOT present: ", avg.at[1, 'distance'])
print()
print("Testing 'avrain' values for normal distribution: ", scipy.stats.normaltest(data['avrain']))
print()
print("Check correlation between number of sites and distance: ")
print(scipy.stats.normaltest(data['NoOfSites']))
print(scipy.stats.normaltest(data['distance']))
print(scipy.stats.spearmanr(data['NoOfSites'], data['distance']))
print()

IsPres = data.loc[data['pres.abs'] == 0, 'altitude']
NotPres = data.loc[data['pres.abs'] == 1, 'altitude']
print("Null: ", scipy.stats.ttest_ind(IsPres, NotPres))
print("Alternative: ", scipy.stats.ttest_ind(IsPres, NotPres, alternative='less'))