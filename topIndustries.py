from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
startUp = pd.read_csv("startup_funding.csv", encoding='utf-8')
df = startUp.copy()
df["AmountInUSD"].fillna(0, inplace=True)
df['IndustryVertical'].dropna(inplace=True)
df['AmountInUSD'] = df['AmountInUSD'].apply(lambda x: float(str(x).replace(",", "")))
df['AmountInUSD'] = pd.to_numeric(df['AmountInUSD'])
df['IndustryVertical'].replace("eCommerce", "Ecommerce", inplace=True)
df['IndustryVertical'].replace("ECommerce", "Ecommerce", inplace=True)
# x = df.groupby('IndustryVertical')['AmountInUSD'].sum().sort_values(ascending=False)
type_funding = df.groupby('IndustryVertical')['AmountInUSD'].sum().sort_values(ascending=False)[0:5]
vertical = type_funding.index
value = type_funding.values
# value2 = x.values
p = np.true_divide(value, value.sum()) * 100
for i in range(len(vertical)):
    print(vertical[i].strip(), format(p[i], '.2f'))