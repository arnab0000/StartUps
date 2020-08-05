from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
startUp = pd.read_csv("startup_funding.csv", encoding='utf-8')
df = startUp.copy()
df['CityLocation'].dropna(inplace=True)
def splitColumn(city):
    return city.split('/')[0].strip()
df['CityLocation'] = df['CityLocation'].apply(splitColumn)
df['CityLocation'].replace("Delhi", "New Delhi", inplace=True)
df['CityLocation'].replace("Delhi", "New Delhi", inplace=True)
df['CityLocation'].replace("bangalore", "Bangalore", inplace=True)
df['AmountInUSD'] = df['AmountInUSD'].apply(lambda x: float(str(x).replace(",", "")))
df['AmountInUSD'] = pd.to_numeric(df['AmountInUSD'])
city_amount = df.groupby('CityLocation')['AmountInUSD'].sum().sort_values(ascending=False)[0:10]
city = city_amount.index
amountCity = city_amount.values
p = np.true_divide(amountCity, amountCity.sum()) * 100
for i in range(len(city)):
    print(city[i], format(p[i], '.2f'))