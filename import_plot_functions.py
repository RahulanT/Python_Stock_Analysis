
import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd
from import_func_stockquery_file import moving_avg ,get_stockinfo_data_1
from scipy.signal import find_peaks
from _datetime import date



def dict_to_dataframe(dict_dataset): ### Changing dictionary to dataframe

    x_prices = dict_dataset['historical']

    x_df = pd.DataFrame(x_prices)

    x_df= x_df[::-1].reset_index(drop = True)
    
    return x_df


def peak_finder(signal):
    
    peaks, _ = find_peaks(signal, distance=20)
#     ret_peak = np.c_(peaks, signal[peaks])
    troughs,_ = find_peaks(-signal , distance =20)

    return peaks,troughs;
    
    
    
def plot_the_dataframe(dataset_dataframe_form , stock_ticker) :

    
    x_prices = dataset_dataframe_form['historical']

    print(x_prices)

    x_df = pd.DataFrame(x_prices)

    x_df= x_df[::-1].reset_index(drop = True)
    
    print(x_df)


   

    date_array = x_df['date'].to_numpy()
    value_array = x_df['adjClose'].to_numpy()
    
    mvg_table_3 = moving_avg(value_array, 50)
    mvg_table_5 = moving_avg(value_array, 200)
    
#     print('the moving average' , mvg_table_3)
#     
    date_datetime = pd.to_datetime(x_df['date'] , format="%Y-%m")
#     day_date_datetime =  pd.to_datetime(x_df['date'] , format="%Y-%m-%d")#    
#     date_index = x_df.set_index('date')
#     
    peaks, troughs = peak_finder(value_array)
#   
    info_df = pd.DataFrame(get_stockinfo_data_1(stock_ticker))
    
#     print(info_df)
  
#     plt.plot(date_datetime[peaks]  
#     
#     #### PLOT FUNCTIOS ###########
#     
    fig, ax = plt.subplots()
    ax.plot(date_datetime[peaks] , value_array[peaks] , 'x') 
    ax.plot(date_datetime[troughs] , value_array[troughs] , 'o')
    ax.plot(date_datetime, value_array , label = 'line 1')
#     plt.plot(date_datetime[49:,]  , mvg_table_3[49:,]  , label = 'moving 3')
#     plt.plot(date_datetime[199:,] , mvg_table_5[199:,] , label = 'moving 5')
#     plt.legend()
#     ax.title(info_df['companyName'][0] + "  " + info_df['symbol'][0] )
     
#     plt.show()
      
    return 0