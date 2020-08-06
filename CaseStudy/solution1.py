# 1. Your Friend has developed the Product and he wants to establish the product startup and he is searching for a perfect location where
#    getting the investment has a high chance. But due to its financial restriction, he can choose only between three locations -  Bangalore,
#    Mumbai, and NCR. As a friend, you want to help your friend deciding the location. NCR include Gurgaon, Noida and New Delhi.
#    Find the location where the most number of funding is done. That means, find the location where startups has received funding maximum
#    number of times. Plot the bar graph between location and number of funding. Take city name "Delhi" as "New Delhi".
#    Check the case-sensitiveness of cities also. That means, at some place instead of "Bangalore", "bangalore" is given.
#    Take city name as "Bangalore". For few startups multiple locations are given, one Indian and one Foreign.
import pandas as pd
import matplotlib.pyplot as plt
startUp = pd.read_csv("startup_funding.csv", encoding='utf-8')
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
plt.bar(location, number)
plt.title('Max number of Fundings')
plt.ylabel('Funding frequency')
plt.xlabel('Cities')
plt.show()