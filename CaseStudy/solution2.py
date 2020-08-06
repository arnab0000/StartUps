# 2. Even after trying for so many times, your friend’s startup could not find the investment. So you decided to take this matter
#    in your hand and try to find the list of investors who probably can invest in your friend’s startup. Your list will increase
#    the chance of your friend startup getting some initial investment by contacting these investors. Find the top 5 investors who
#    have invested maximum number of times (consider repeat investments in one company also). In a startup, multiple investors might
#    have invested. So consider each investor for that startup. Ignore undisclosed investors.
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
startUp = pd.read_csv("startup_funding.csv", encoding='utf-8')
df = startUp.copy()
df['CityLocation'].dropna(inplace=True)
def splitColumn(city):
    return city.split('/')[0].strip()
df['CityLocation'] = df['CityLocation'].apply(splitColumn)
df['CityLocation'].replace("Delhi", "New Delhi", inplace=True)
df['CityLocation'].replace("bangalore", "Bangalore", inplace=True)
df['InvestorsName'].replace("Undisclosed investors", "Undisclosed Investors", inplace=True)
# df = df[(df['CityLocation'] == 'Bangalore') | (df['CityLocation'] == 'Gurgaon') | (df['CityLocation'] == 'Mumbai') | (df['CityLocation'] == 'Noida') | (df['CityLocation'] == 'New Delhi')]
# df['InvestorsName'].dropna(inplace=True)
# type_funding = df.groupby('InvestorsName').size().sort_values(ascending=False)[1:6]
# # print(type_funding.head())
# investorName = type_funding.index
# number = type_funding.values
# for i in range(len(investorName)):
#     print(investorName[i].strip(), number[i])
df['InvestorsName'].dropna(inplace=True)
name_investors = {}
def investor(name):
    # print(name)
    name = name.split(",")
    for i in name:
        name_investors[i.strip()] = name_investors.get(i.strip(), 0) + 1
df['InvestorsName'] = df['InvestorsName'].apply(investor)
k = Counter(name_investors)
highest = k.most_common(6)
for i in range(0, 6):
    if highest[i][0] != "Undisclosed Investors":
        print(highest[i][0], highest[i][1])

