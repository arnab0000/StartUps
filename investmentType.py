from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
startUp = pd.read_csv("startup_funding.csv", encoding='utf-8')
df = startUp.copy()
df["AmountInUSD"].fillna(0, inplace=True)
df['InvestmentType'].dropna(inplace=True)
print(df)
df['AmountInUSD'] = df['AmountInUSD'].apply(lambda x: float(str(x).replace(",", "")))
df['AmountInUSD'] = pd.to_numeric(df['AmountInUSD'])
df['InvestmentType'].replace("SeedFunding", "Seed Funding", inplace=True)
df['InvestmentType'].replace("PrivateEquity", "Private Equity", inplace=True)
df['InvestmentType'].replace("Crowd funding", "Crowd Funding", inplace=True)
type_funding = df.groupby('InvestmentType')['AmountInUSD'].sum().sort_values(ascending=False)
typeAmount = type_funding.values
type_investment = type_funding.index
p = np.true_divide(typeAmount, typeAmount.sum()) * 100
x, y = [], []
for i in range(len(type_investment)):
    x.append(p[i])
    y.append(type_investment[i])
    print(type_investment[i], format(p[i], '.2f'))
plt.axis('equal')
plt.pie(x, labels=y)
plt.show()