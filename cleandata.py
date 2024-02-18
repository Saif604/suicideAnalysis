import pandas as pd

df = pd.read_csv('./Container/data.csv')

df.drop('country-year',axis=1,inplace=True)

df.to_csv('./cleanData.csv')