import requests as req
import json
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import matplotlib.dates as mpl_dates
import matplotlib.ticker as mticker
from _datetime import date

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


def dict_to_dataframe(dict_dataset): ### Changing dictionary to dataframe

    x_prices = dict_dataset['historical']

    x_df = pd.DataFrame(x_prices)

    x_df= x_df[::-1].reset_index(drop = True)
    
    return x_df

def minute_data(stock_ticker):

    stock_info_url = ("https://financialmodelingprep.com/api/v3/historical-chart/1min/"  +  stock_ticker   + "?apikey=ee74a2831784bf661aeeeefb557a43cd")
    response = req.get(stock_info_url)
    # data = response.read().decode("utf-8")
    # return json.loads(data)
    data = response.json()

    return data

def inst_data(stock_ticker):
    
    stock_info_url = ("https://financialmodelingprep.com/api/v3/quote-short/" + stock_ticker + "?apikey=ee74a2831784bf661aeeeefb557a43cd")
    response = req.get(stock_info_url)
    # data = response.read().decode("utf-8")
    # return json.loads(data)
    data = response.json()

    return data

    
x = minute_data('MSFT')

candle_data = pd.DataFrame(x)

# print(candle_data)

candle_data['Datetime'] = pd.to_datetime(candle_data['date'])
candle_data  = candle_data.set_index('Datetime')

print(candle_data)

candle_data = candle_data.loc[:, ['open', 'high', 'low', 'close' , 'volume']]

mpf.plot(candle_data ,type ='candle')


# candle_data_rsi = candle_data.loc[:, ['open', 'high', 'low', 'close' , 'volume']].copy()
# 
# # pd.fillna(candle_data)
# 
# # print('rsi' , candle_data_rsi)
#  
#  
# candle_data_rsi['close'] = computeRSI(candle_data_rsi['close'], 14)
# print('rsi' , candle_data_rsi)
#  
# candle_data_rsi = candle_data_rsi.fillna(0)
# print('rsi' , candle_data_rsi)
#      
# mpf.plot(candle_data_rsi)   