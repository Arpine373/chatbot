import pandas as pd
import matplotlib.pyplot as plt

file_url='https://people.sc.fsu.edu/~jburkardt/data/csv/homes.csv'
dataframe=pd.read_csv(file_url)

print(dataframe.head())

print(dataframe.shape)

print(dataframe.columns.values)

print(dataframe.isna().head())

print(dataframe.isna().shape)

print(dataframe.info())

print(dataframe.describe())

print(dataframe.drop('Sell',axis=1).head())

print(dataframe.sum())

print(dataframe.mean())

print(dataframe.sort_values(by=["Beds"],ascending=False))

print(dataframe.groupby(['Rooms'], as_index=False))

dataframe.plot()
plt.show()

