# 4. Even after putting so much effort in finding the probable investors, it didn't turn out to be helpful for your friend. So you went
#    to your investor friend to understand the situation better and your investor friend explained to you about the different Investment
#    Types and their features. This new information will be helpful in finding the right investor. Since your friend startup is at an
#    early stage startup, the best-suited investment type would be - Seed Funding and Crowdfunding. Find the top 5 investors who have
#    invested in a different number of startups and their investment type is Crowdfunding or Seed Funding. Correct spelling of investment
#    types are - "Private Equity", "Seed Funding", "Debt Funding", and "Crowd Funding". Keep an eye for any spelling mistake. You can find
#    this by printing unique values from this column. There are many errors in startup names. Ignore correcting all, just handle the
#    important ones - Ola, Flipkart, Oyo and Paytm.

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
        inves_type = row['InvestmentType']
        if not pd.isnull(investors) and investors != '' and not pd.isnull(startup) and startup != '' and not pd.isnull(inves_type):
            if inves_type == 'SeedFunding' or inves_type == 'Seed Funding' or inves_type == 'Crowd funding' or inves_type == 'Crowd Funding':
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
                    if i == '' or i == 'Undisclosed Investors' or i == 'Undisclosed investors':
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
plt.bar(invstrs, arr, width=0.6, edgecolor='black')
plt.xticks(rotation=40)
plt.show()