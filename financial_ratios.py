from scipy.signal import argrelextrema
from import_func_stockquery_file import get_year_range_price_data as query_func
from import_func_stockquery_file import moving_avg as m_avg
from import_plot_functions import plot_the_dataframe as plot_func 

import requests as req
import numpy as np
import json
from urllib.request import urlopen
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from import_func_stockquery_file import get_stockinfo_data_1
from import_plot_functions import dict_to_dataframe as dtd

tick = 'AAPL'

url_2 = "https://financialmodelingprep.com/api/v3/ratios/" + tick + "?limit=40&apikey=ee74a2831784bf661aeeeefb557a43cd"

url_3 = "https://financialmodelingprep.com/api/v3/stock-screener?industry=Semiconductors&sector=Technology&apikey=ee74a2831784bf661aeeeefb557a43cd"

# url_4 = 

def get_datas(url):
     
    response = req.get(url)
    # data = response.read().decode("utf-8")
    # return json.loads(data)
    data = json.loads(response.text)
     
    return data
# 
# fin_ratio = pd.DataFrame(get_ratios(url_2))
# 
# fin_ratio = fin_ratio.iloc[::-1]
# 
# print(fin_ratio.iloc[::-1])
# 
# plot_list = ['returnOnEquity' , 'debtEquityRatio' , 'priceToBookRatio' , 'priceEarningsRatio' , 'priceEarningsToGrowthRatio'];

# column_s = ['symbol' , 'price' , 'marketCap']
# 
# mu = pd.DataFrame(get_datas(url_2) , columns =column_s)
 
# mu = pd.DataFrame(mu, columns=column_s)
# print(mu)
# mu = mu.sort_values(by = 'price'  ,ascending = False)
#  
# print(mu)
 
historical_val_dict = query_func(tick , '2015' , '2017')
   
# print(historical_val_dict)
   
   
plot_func(historical_val_dict , tick)



# for i in plot_list:
#      
# #     fin_ratio['returnOnEquity']
#     (fig, ax) = plt.subplots()
#     ax.plot(fin_ratio['date'] , fin_ratio[i])
#     plt.title(i)
#     plt.show()



# # Plot main graph.
# (fig, ax) = plt.subplots()
# ax.plot(fin_ratio['Date'] , fin_ratio['Values'])

stock_data = query_func(tick, '2015', '2017')


stock_data = dtd(stock_data)

print(stock_data)

def computeRSI(data , time_window):
    
    diff = data.diff(1).dropna()        # diff in one field(one day)

    #this preservers dimensions off diff values
    up_chg = 0 * diff
    down_chg = 0 * diff
    
    # up change is equal to the positive difference, otherwise equal to zero
    up_chg[diff > 0] = diff[ diff>0 ]
    
    # down change is equal to negative deifference, otherwise equal to zero
    down_chg[diff < 0] = diff[ diff < 0 ]
    
    # check pandas documentation for ewm
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ewm.html
    # values are related to exponential decay
    # we set com=time_window-1 so we get decay alpha=1/time_window
    up_chg_avg   = up_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    down_chg_avg = down_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    
    rs = abs(up_chg_avg/down_chg_avg)
    rsi = 100 - 100/(1+rs)
    
    return rsi
    
    
stock_data['RSI'] = computeRSI(stock_data['close'], 14)

print(stock_data)

fig, ax = plt.subplots()
    
ax.plot(pd.to_datetime(stock_data['date'] , format="%Y-%m") , stock_data['RSI'])    
ax.axhline(0, linestyle='--', alpha=0.1)
ax.axhline(20, linestyle='--', alpha=0.5)
ax.axhline(30, linestyle='--')

ax.axhline(70, linestyle='--')
ax.axhline(80, linestyle='--', alpha=0.5)
ax.axhline(100, linestyle='--', alpha=0.1)

plt.show()    
    