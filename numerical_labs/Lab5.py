import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print('TimeSeries:')
ts1 = pd.Series([0,1,2,3,4,5,6,7,8,9,10], index=pd.date_range('2022-09-01', periods=11, freq='2MS'))
ts2 = pd.Series([0,1,2,3], index=pd.date_range('2022-12-29', periods=4, freq='8H'))
print(ts1)
print()
print(ts2)
print()
print('Subarrays:')
print()
print(ts1.loc['2023-04':'2023-08'])
print()
print(ts2.loc['2022-12-29'])

data = pd.read_csv('PythonLabs/BChain.csv', index_col=['Date'], parse_dates=True)
bitc = data['Bitcoins_in_circulation']

bitc.plot()
plt.title("General change of amount of bitcoins in circulation")
plt.ylabel("Bitcoins in circulation")
plt.xlabel("Year")
plt.show()

bitc.loc['2017'].plot()
plt.title("Change of amount of bitcoins in circulation in 2017")
plt.ylabel("Bitcoins in circulation")
plt.xlabel("Month")
plt.show()

bitc.loc['2016-04'].plot()
plt.title("Change of amount of bitcoins in circulation in April 2016")
plt.ylabel("Bitcoins in circulation")
plt.xlabel("Day")
plt.show()

bitc.loc['2010-02':'2015-12'].plot()
plt.title("Change of amount of bitcoins in circulation from Feb 2010 to Dec 2015")
plt.ylabel("Bitcoins in circulation")
plt.xlabel("Year")
plt.show()

sns.lineplot(bitc.loc['2011'], color='red')
sns.lineplot(bitc.loc['2015'], color='green')
plt.title("Bitcoins in circulation in 2011 and 2015")
plt.xlabel("Year")
plt.show()

block = data['BlockSize']
print("Max size of block in 2012: ", block.loc['2012'].max())
print("Max size of block in every year: ")
print(block.resample('Y').max())
print()
print("Max size of block in every month of 2017: ")
print(block.loc['2017'].resample('M').max())
print()

data['change']=data['BlockSize'].pct_change()
change = data['change']
a = change.loc['2015-09':'2015-11'].asfreq(freq='4D')
plt.lineplot(a.index, a.values, color='green')
plt.xlabel('Date')
plt.ylabel('Percentage change of block size')
plt.title('Percentage change of block size in autumn of 2015 (every 4 days)')
plt.show()


block.loc['2016'].rolling('30D').mean().plot()
#b = block.loc['2016'].resample('M').mean()
#plt.plot(b.index, b.values, color='blue')
plt.title('Rolling average of block size in 2016 by month')
plt.xlabel('Date')
plt.ylabel('Average of block size')
plt.show()
