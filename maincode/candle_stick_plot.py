import import_func_stockquery_file
import import_plot_functions 
import pandas as pd
import matplotlib.dates as mpl_dates
import matplotlib.ticker as mticker
import mplfinance as mpf
#from matplotlib.finance import candlestick2_ohlc

stock_ticker = 'AAPL'

get_func = import_func_stockquery_file.get_year_range_price_data

historical_val_dict = get_func(stock_ticker , '2014' , '2017')

candle_data = import_plot_functions.dict_to_dataframe(historical_val_dict)

# CANDLE_STICK_PLOTTING

print(candle_data)

pd.DatetimeIndex(candle_data['date'])
candle_data.set_index('date')
# candle_data = candle_data.loc[:, ['open', 'high', 'low', 'close' , 'volume']]

mpf.plot(candle_data ,type ='candle' ,style='charles')

candle_data_rsi = pd.DataFrame(candle_data)
candle_data_rsi['close'] = computeRSI(candle_data['close'], 14)

print(candle_data_rsi)

# fig, ax = plt.subplots()
    
mpf.plot(candle_data_rsi)    

# ax.axhline(0, linestyle='--', alpha=0.1)
# ax.axhline(20, linestyle='--', alpha=0.5)
# ax.axhline(30, linestyle='--')
# 
# ax.axhline(70, linestyle='--')
# ax.axhline(80, linestyle='--', alpha=0.5)
# ax.axhline(100, linestyle='--', alpha=0.1)

mpf.show()    