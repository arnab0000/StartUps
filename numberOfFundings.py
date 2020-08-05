import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
startUp = pd.read_csv("startup_funding.csv")
df = startUp.copy()
year = [_ for _ in range(2015, 2018, 1)]
x = []
for i in year:
    y = str(i)
    yearDF = df[df["Date"].str.contains(y)]
    noOfFunding = yearDF.shape[0]
    x.append(noOfFunding)

plt.plot(year, x)
i = 0
while i < 3:
    print(year[i], x[i])
    i += 1
plt.show()
