# 3. After re-analysing the dataset you found out that some investors have invested in the same startup at different number of funding
#    rounds. So before finalising the previous list, you want to improvise it by finding the top 5 investors who have invested in
#    different number of startups. This list will be more helpful than your previous list in finding the investment for your friend
#    startup. Find the top 5 investors who have invested maximum number of times in different companies. That means, if one investor has
#    invested multiple times in one startup, count one for that company. There are many errors in startup names. Ignore correcting all,
#    just handle the important ones - Ola, Flipkart, Oyo and Paytm.

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

invest_count = {}
with open('startup_funding.csv', encoding='utf8') as obj:
    file_data = csv.DictReader(obj, skipinitialspace=True)
    for row in file_data:
        investors = row['InvestorsName']
        startup = row['StartupName']
        if not pd.isnull(investors) and investors != '' and not pd.isnull(startup) and startup != '':
            lwr_str = startup.lower()
            l1 = lwr_str.split()  # to chk against oyo rooms
            l2 = lwr_str.split('.')  # To chk against flipkart.com

            # if 'ola' in s_name.lower(): # can't do like that bcz it will also include startups like kolabro which is not ola

            if 'ola' in l1 or 'ola' in l2 or 'olacabs' in l1:
                req_startup = 'Ola'
            elif 'flipkart' in l1 or 'flipkart' in l2:
                req_startup = 'Flipkart'
            elif 'oyo' in l1 or 'oyo' in l2 or 'oyorooms' in l1:
                req_startup = 'Oyo'
            elif 'paytm' in l1 or 'paytm' in l2:
                req_startup = 'Paytm'
            else:
                req_startup = startup

            inves_list = [investr.strip() for investr in investors.split(',')]
            for i in inves_list:
                if i == '':
                    continue
                if invest_count.get(i, -1) == -1:
                    invest_count[i] = set()
                invest_count[i].add(req_startup)

invest_count_arr = list(invest_count.items())
# print(invest_count_arr)
invest_count_arr.sort(key=lambda x: len(x[1]))
req_arr = invest_count_arr[::-1]
for i in range(5):
    print(req_arr[i][0], len(req_arr[i][1]))

arr = [len(req_arr[i][1]) for i in range(5)]
invstrs = [req_arr[i][0] for i in range(5)]
plt.pie(arr, labels=invstrs, autopct='%.2f')
plt.show()

# from collections import Counter
# import pandas as pd
# startUp = pd.read_csv("startup_funding.csv", encoding='utf-8')
# df = startUp.copy()
# # df['CityLocation'].dropna(inplace=True)
# # def splitColumn(city):
# #     return city.split('/')[0].strip()
# # df['CityLocation'] = df['CityLocation'].apply(splitColumn)
# # df['CityLocation'].replace("Delhi", "New Delhi", inplace=True)
# # df['CityLocation'].replace("bangalore", "Bangalore", inplace=True)
# df['InvestorsName'].replace("Undisclosed investors", "Undisclosed Investors", inplace=True)
# # df = df[(df['CityLocation'] == 'Bangalore') | (df['CityLocation'] == 'Gurgaon') | (df['CityLocation'] == 'Mumbai') | (df['CityLocation'] == 'Noida') | (df['CityLocation'] == 'New Delhi')]
# df['InvestorsName'].dropna(inplace=True)
# df['StartupName'].replace('Paytm Marketplace','Paytm',inplace=True)
# df['StartupName'].replace('Oyo Rooms','Oyo',inplace = True)
# df['StartupName'].replace('OyoRooms','Oyo',inplace = True)
# df['StartupName'].replace('Oyorooms','Oyo',inplace = True)
# df['StartupName'].replace('OYO Rooms','Oyo',inplace=True)
# df['StartupName'].replace('Paytm Marketplace','Paytm',inplace = True)
# df['StartupName'].replace('flipkart.com','Flipkart',inplace = True)
# df['StartupName'].replace('Ola Cabs','Ola',inplace = True)
# df['StartupName'].replace('Olacabs','Ola',inplace = True)
# df['StartupName'].replace('OYO Rooms','Oyo',inplace=True)
# df['StartupName'].replace('Flipkart.com','Flipkart',inplace = True)
# df['StartupName'].dropna(inplace=True)
# # df['InvestorsName'].dropna(inplace=True)
# name_investors = {}
# def investor(name):
#     x = []
#     name = name.split(",")
#     for i in name:
#         s = i.strip()
#         if s not in x:
#             name_investors[s] = name_investors.get(s, 0) + 1
#             x.append(s)
#
# df['InvestorsName'] = df['InvestorsName'].apply(investor)
# k = Counter(name_investors)
# highest = k.most_common(6)
# for i in range(0, 6):
#     if highest[i][0] != "Undisclosed Investors":
#         print(highest[i][0], highest[i][1])

