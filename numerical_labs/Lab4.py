import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('PythonLabs/insurance.csv')
#print(data)
data['region'].value_counts().sort_index().plot.barh()
plt.title("Number of people in every region")
plt.xlabel("amount")
plt.show()

sns.barplot(data=data, x='region', y='age', estimator=np.min, palette = "Greens")
plt.title("Minimum age of every region")
plt.ylabel("minimum age")
plt.show()

children = pd.pivot_table(data,
values="children",index="region",columns="sex", aggfunc=np.mean)
ax = children.plot(kind="barh",alpha=0.7)
plt.title("Average number of children")
plt.show()

plt.hist(data['bmi'], color='green', edgecolor='black')
plt.title("Body mass index. All people")
plt.ylabel("number of people")
plt.xlabel("body mass index")
plt.show()

g = sns.FacetGrid(data, col='smoker')
g = g.map(sns.histplot, 'bmi')
plt.show()

sns.boxplot(x='expenses', data=data)
plt.title("Boxplot of general expenses")
plt.show()

sns.boxplot(x='region', y='expenses', data=data)
plt.title("Boxplot of expenses by region")
plt.show()

plt.scatter(data['age'], data['expenses'], c='g', s=50, alpha=0.7)
plt.title("Age and expenses scatter diagram")
plt.show()

plt.scatter(data['bmi'], data['expenses'], c='g', s=50, alpha=0.7)
plt.title("Body mass index and expenses scatter diagram")
plt.show()

print("Correlation coefficient between age and expenses: ", data['expenses'].corr(data['age']))
print("Correlation coefficient between BMI and expenses: ", data['expenses'].corr(data['bmi']))