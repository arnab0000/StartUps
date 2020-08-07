# 5. Due to your immense help, your friend startup successfully got seed funding and it is on the operational mode. Now your friend wants
#    to expand his startup and he is looking for new investors for his startup. Now you again come as a saviour to help your friend and
#    want to create a list of probable new new investors. Before moving forward you remember your investor friend advice that finding the
#    investors by analysing the investment type. Since your friend startup is not in early phase it is in growth stage so the best-suited
#    investment type is Private Equity. Find the top 5 investors who have invested in a different number of startups and their investment
#    type is Private Equity. Correct spelling of investment types are - "Private Equity", "Seed Funding", "Debt Funding", and "Crowd Funding".
#    Keep an eye for any spelling mistake. You can find this by printing unique values from this column.There are many errors in startup
#    names. Ignore correcting all, just handle the important ones - Ola, Flipkart, Oyo and Paytm.
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
            if inves_type == 'Private Equity' or inves_type == 'privateEquity' or inves_type == 'PrivateEquity' or inves_type == 'Private equity':
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