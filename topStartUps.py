from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
startUp = pd.read_csv("startup_funding.csv", encoding='utf-8')
df = startUp.copy()
df['InvestorsName'].dropna(inplace=True)
df['StartupName'].replace('Paytm Marketplace','Paytm',inplace=True)
df['StartupName'].replace('Oyo Rooms','Oyo',inplace = True)
df['StartupName'].replace('OyoRooms','Oyo',inplace = True)
df['StartupName'].replace('Oyorooms','Oyo',inplace = True)
df['StartupName'].replace('OYO Rooms','Oyo',inplace=True)
df['StartupName'].replace('Paytm Marketplace','Paytm',inplace = True)
df['StartupName'].replace('flipkart.com','Flipkart',inplace = True)
df['StartupName'].replace('Flipkart.com','Flipkart',inplace = True)
df['StartupName'].replace('Ola Cabs','Ola',inplace = True)
df['StartupName'].replace('Olacabs','Ola',inplace = True)
df['StartupName'].replace('OYO Rooms','Oyo',inplace=True)
df['AmountInUSD'] = df['AmountInUSD'].apply(lambda x: float(str(x).replace(",", "")))
df['AmountInUSD'] = pd.to_numeric(df['AmountInUSD'])
type_funding = df.groupby('StartupName')['AmountInUSD'].sum().sort_values(ascending=False)[0:5]
names = type_funding.index
for i in range(len(names)):
    print(names[i])