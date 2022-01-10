import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('forex_usd_data.csv')
countries = list(data.columns)
index = list(range(len(data[countries[0]])))

for i in range(len(countries)-1):
    plt.plot(index,list(data[countries[i +1]]))
    plt.ylabel(countries[i])
    plt.show()

