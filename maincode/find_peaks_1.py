from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
import numpy as np
import requests as req
import numpy as np
import json
from urllib.request import urlopen
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

# Generate random data.
data_x = np.arange(start = 0, stop = 25, step = 1, dtype='int')
data_y = np.random.random(25)*6
 
# Find peaks(max).
peak_indexes = argrelextrema(data_y, np.greater)
peak_indexes = peak_indexes[0]

from_year = '2015'
to_year = '2016'


url_2 = ("https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?from=" + from_year + "-03-12&to=" + to_year + "-03-12&apikey=ee74a2831784bf661aeeeefb557a43cd")

def get_jsonparsed_data(url):
    
    response = req.get(url)
    # data = response.read().decode("utf-8")
    # return json.loads(data)
    data = json.loads(response.text)
    return data


historical_val_dict = get_jsonparsed_data(url_2)

x_prices = historical_val_dict['historical']

x_dict = {}
x_dates = []
x_close = []

for iteration in range(len(x_prices)):

    x_dates.append(x_prices[iteration]['date'])
    x_close.append(x_prices[iteration]['close'])
    #x_dict[x_prices[iteration]['date']] =  x_prices[iteration]['close']

x_close.reverse()
x_dates.reverse()

x_df = pd.DataFrame({'Date' : x_dates , 'Values' : x_close})

x_df_datetime = pd.to_datetime(x_df['Date'])

print(x_df)

x_datetime_index = pd.DatetimeIndex(x_df_datetime.values)

print(x_datetime_index)

x_df2 = x_df.set_index(x_datetime_index)

print(x_df2)

print('----------------------------------------------------------')

# resampled_data = x_df2.resample('M').mean()

# x_array = np.array(resampled_data['Values'])

# resampled_data['Date'] = resampled_data.index.values



'''

x_dfn = x_df.convert_dtypes()
print(resampled_data)
# print(x_dfn)
print(resampled_data.dtypes)
x_dfn = x_dfn.astype({'Date' : 'datetime64[ns]'})
print('x_dfn is :' , x_dfn.dtypes)
print('x_dfn' , x_dfn)

x_df_new = x_dfn.loc[x_dfn['Date'].isin(resampled_data['Date'])]

print(x_df_new)



x_df_new = x_df_new.reset_index()

x_array = np.array(x_df_new['Values'])

'''
x_df2 = x_df2.reset_index()


x_array = np.array(x_df2['Values'])


print('---------------------------------------------------')


# Find peaks(max).
peak_indexes = argrelextrema(x_array, np.greater)
peak_indexes = peak_indexes[0]

print(peak_indexes)

# Find valleys(min).
valley_indexes = argrelextrema(x_array, np.less)
valley_indexes = valley_indexes[0]
 
# Plot main graph.
(fig, ax) = plt.subplots()
ax.plot(x_df2['Date'] , x_df2['Values'])
 


# Plot peaks.
#peak_x = peak_indexes
print('---------------------------------------------------------')
peak_y = x_df2.loc[peak_indexes]
print(peak_y)
ax.plot(peak_y['Date'] , peak_y['Values'], marker='o', linestyle='dashed', color='green', label="Peaks")
plt.show()

