import import_func_stockquery_file
import import_plot_functions 
import pandas as pd
import matplotlib.dates as mpl_dates
import matplotlib.ticker as mticker
import mplfinance as mpf
import matplotlib.pyplot as plt


#from matplotlib.finance import candlestick2_ohlc

stock_ticker = 'AAPL'

get_func = import_func_stockquery_file.get_year_range_price_data

historical_val_dict = get_func(stock_ticker , '2014' , '2017')

candle_data = import_plot_functions.dict_to_dataframe(historical_val_dict)

# CANDLE_STICK_PLOTTING
datetime_index = pd.DatetimeIndex(pd.to_datetime(candle_data['date']))
candle_data = candle_data.loc[:, ['date', 'open', 'high', 'low', 'close' , 'volume']]

candle_data.set_index(datetime_index , inplace = True )

print(type(candle_data))

mpf.plot(candle_data , type = 'candle' ,style='charles')
