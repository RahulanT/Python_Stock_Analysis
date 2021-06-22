from import_func_stockquery_file import get_year_range_price_data as query_func
from import_func_stockquery_file import earnings_data as query_earn_func
from import_func_stockquery_file import moving_avg as m_avg

from import_plot_functions import plot_the_dataframe as plot_func 
from import_plot_functions import peak_finder as pf
import pandas as pd
# from import_plot_functions import dict_earnings


def list_earnings(dict_dataset):  
    
    earnings_date = [];
    
    for iteration in range(len(dict_dataset)):
        
        earnings_date.append(dict_dataset[iteration]['date']);

#     x_df = pd.DataFrame(earnings) 
    print (type(earnings_date))
    
    return earnings_date




stock_ticker = 'MU'



historical_val_dict = query_func(stock_ticker , '2018' , '2020')

# print(historical_val_dict)


plot_func(historical_val_dict , stock_ticker)



    
