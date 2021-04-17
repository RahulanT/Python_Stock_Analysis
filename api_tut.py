import requests as req
import numpy as np
import json
from urllib.request import urlopen
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

url_1 = ("https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=ee74a2831784bf661aeeeefb557a43cd")
url_2 = ("https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?serietype=line&apikey=ee74a2831784bf661aeeeefb557a43cd")
url_3 = ("https://financialmodelingprep.com/api/v3/ratios/AAPL?period=quarter&limit=140&apikey=ee74a2831784bf661aeeeefb557a43cd")


def get_jsonparsed_data(url):
    
    response = req.get(url)
    # data = response.read().decode("utf-8")
    # return json.loads(data)
    data = json.loads(response.text)
    return data

profile_dict = get_jsonparsed_data(url_1)

historical_val_dict = get_jsonparsed_data(url_2)

financial_ratios = get_jsonparsed_data(url_3)

x_prices = historical_val_dict['historical']

x_dict = {}
x_dates = []
x_close = []

for iteration in range(len(x_prices)):

    x_dates.append(x_prices[iteration]['date'])
    x_close.append(x_prices[iteration]['close'])
    #x_dict[x_prices[iteration]['date']] =  x_prices[iteration]['close']

x_dates.reverse()
x_close.reverse()

df = pd.DataFrame({'Date': x_dates , 'Values' : x_close})

df['Date'] = pd.to_datetime(df['Date'] , format = '%Y-%m-%d')

df2 = df.resample('M' , on = 'Date').mean().reset_index()

fin_date = []
fin_PEratio = []
fin_PBratio = []

for iteration in range(len(financial_ratios)):
    fin_date.append(financial_ratios[iteration]['date'])
    fin_PEratio.append(financial_ratios[iteration]['priceEarningsRatio'])
    fin_PBratio.append(financial_ratios[iteration]['priceToBookRatio'])

fin_date.reverse()
fin_PBratio.reverse()
fin_PEratio.reverse()


finan_ratio_df = pd.DataFrame({'Date': fin_date , 'PEratio' : fin_PEratio , 'PBratio' : fin_PBratio})

finan_ratio_df['Date'] = pd.to_datetime(finan_ratio_df['Date'] , format = '%Y-%m-%d')


#plt.plot(df2['Date'], df2['Values'], color = 'red')

#print(finan_ratio_df)

#plt.plot(finan_ratio_df['Date'] , finan_ratio_df['PBratio'])
#plt.plot(finan_ratio_df['Date'] , finan_ratio_df['PEratio'])


df['3_Day_rolling'] =  df.rolling(7, center=True).mean()
print(df.head(10))

plt.plot(df['Date'] , df['Values'])
plt.plot(df2['Date'] , df2['Values'])
plt.plot(df['Date'] , df['3_Day_rolling'])

plt.show()


