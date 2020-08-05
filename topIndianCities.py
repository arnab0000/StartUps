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
df['CityLocation'].replace("banglore", "Banglore", inplace=True)
counts = df['CityLocation'].value_counts()[0:10]
city = counts.index
number = counts.values
for i in range(len(city)):
    print(city[i], number[i])
plt.axis('equal')
plt.pie(number, labels=city)
plt.show()
# print(df)
# d = {}
# for i in df:
#     x = i.lower().strip()
#     if x == 'delhi':
#         x = 'new delhi'
#     if x in d:
#         d[x] += 1
#     else:
#         d[x] = 1
#
# k = Counter(d)
# state, number = [], []
# highest = k.most_common(10)
# for i in range(10):
#     if highest[i][0] == 'new delhi':
#         state.append('New Delhi')
#         number.append(highest[i][1])
#     else:
#         z = highest[i][0]
#         a = z[0]
#         z = a.upper() + z[1:]
#         state.append(z)
#         number.append(highest[i][1])
# plt.axis('equal')
# plt.pie(number, labels=state)
# j = 0
# while j < 10:
#     print(state[j], number[j])
#     j += 1
# plt.show()
