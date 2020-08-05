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
df['StartupName'].replace('Ola Cabs','Ola',inplace = True)
df['StartupName'].replace('Olacabs','Ola',inplace = True)
df['StartupName'].replace('OYO Rooms','Oyo',inplace=True)
df['StartupName'].replace('Flipkart.com','Flipkart',inplace = True)
type_funding = df.groupby('StartupName').size().sort_values(ascending = False)[0:5]
name = type_funding.index
number = type_funding.values
for i in range(len(name)):
    print(name[i], int(number[i]))