# 1. Your Friend has developed the Product and he wants to establish the product startup and he is searching for a perfect location where
#    getting the investment has a high chance. But due to its financial restriction, he can choose only between three locations -  Bangalore,
#    Mumbai, and NCR. As a friend, you want to help your friend deciding the location. NCR include Gurgaon, Noida and New Delhi.
#    Find the location where the most number of funding is done. That means, find the location where startups has received funding maximum
#    number of times. Plot the bar graph between location and number of funding. Take city name "Delhi" as "New Delhi".
#    Check the case-sensitiveness of cities also. That means, at some place instead of "Bangalore", "bangalore" is given.
#    Take city name as "Bangalore". For few startups multiple locations are given, one Indian and one Foreign.
import pandas as pd
import matplotlib.pyplot as plt
startUp = pd.read_csv("startup_funding.csv", encoding='utf-8', skipinitialspace=True)
df = startUp.copy()
df['CityLocation'].dropna(inplace=True)
def splitColumn(city):
    return city.split('/')[0].strip()
df['CityLocation'] = df['CityLocation'].apply(splitColumn)
df['CityLocation'].replace("Delhi", "New Delhi", inplace=True)
df['CityLocation'].replace("bangalore", "Bangalore", inplace=True)
df = df[(df['CityLocation'] == 'Bangalore') | (df['CityLocation'] == 'Gurgaon') | (df['CityLocation'] == 'Mumbai') | (df['CityLocation'] == 'Noida') | (df['CityLocation'] == 'New Delhi')]
type_funding = df.groupby('CityLocation').size().sort_values(ascending = False)[0:5]
# print(type_funding)
location = type_funding.index
number = type_funding.values
for i in range(len(location)):
    print(location[i], number[i])
plt.bar(location, number)
plt.title('Max number of Fundings')
plt.ylabel('Funding frequency')
plt.xlabel('Cities')
plt.show()

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# data=pd.read_csv("startup_funding.csv",skipinitialspace=True)
# data.head()
# data.CityLocation.dropna(inplace=True)
# data.CityLocation.replace("Delhi","New Delhi",inplace=True)
# data.CityLocation.replace("bangalore","Bangalore",inplace=True)
# cities=["Bangalore","Mumbai","Gurgaon","Noida","New Delhi"]
# tno_invest={}
# for i in data.CityLocation:
#     i=i.split("/")
#     for city in i:
#         if city.strip() in cities:
#             tno_invest[city.strip()]=tno_invest.get(city.strip(),0)+1
# tno_city=list(tno_invest)
# tno_value=list(tno_invest.values())
# for i in range(len(tno_city)):
#     print(tno_city[i], tno_value[i])
# #graph plotting
# #bar graph
# plt.bar(tno_city,tno_value)
# plt.show()
# print(tno_invest)