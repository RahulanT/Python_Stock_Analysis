import requests as req
import json
import math
import numpy as np
from scipy.signal import find_peaks


def peak_valleys_finder(signal):
    
    peaks, _ = find_peaks(signal, distance=20)
#     ret_peak = np.c_(peaks, signal[peaks])
    troughs,_ = find_peaks(-signal , distance =20)

    return peaks,troughs;
    

def get_stockinfo_data_1(stock_ticker):

    stock_info_url = ("https://financialmodelingprep.com/api/v3/profile/" + stock_ticker +"?apikey=ee74a2831784bf661aeeeefb557a43cd")

    response = req.get(stock_info_url)
    # data = response.read().decode("utf-8")
    # return json.loads(data)
    data = response.json()
    return data


def get_full_historic_price_data(stock_ticker):

    stock_full_historic_price_url = ("https://financialmodelingprep.com/api/v3/historical-price-full/" + stock_ticker + "?serietype=line&apikey=ee74a2831784bf661aeeeefb557a43cd")

    response = req.get(stock_full_historic_price_url)
    # data = response.read().decode("utf-8")
    # return json.loads(data)
    data = json.loads(response.text)
    return data


def get_stockinfo_data(stock_ticker):

    stock_financial_ratio_url = ("https://financialmodelingprep.com/api/v3/ratios/"+ stock_ticker +"?period=quarter&limit=140&apikey=ee74a2831784bf661aeeeefb557a43cd")

    response = req.get(stock_financial_ratio_url)
    # data = response.read().decode("utf-8")
    # return json.loads(data)
    data = json.loads(response.text)
    return data

from_year = '2016'
to_year = '2017'



def get_year_range_price_data(stock_ticker , from_year , to_year):

    
    
    url_2 = ("https://financialmodelingprep.com/api/v3/historical-price-full/" + stock_ticker + "?from=" + from_year + "-03-12&to=" + to_year + "-03-12&apikey=ee74a2831784bf661aeeeefb557a43cd")

    response = req.get(url_2)
    # data = response.read().decode("utf-8")
    # return json.loads(data)
    data = json.loads(response.text)
    return data


def earnings_data(stock_ticker):

    stock_earnings_date_url =("https://financialmodelingprep.com/api/v3/income-statement/" + stock_ticker + "?period=quarter&limit=400&apikey=ee74a2831784bf661aeeeefb557a43cd")
    response = req.get(stock_earnings_date_url)
    # data = response.read().decode("utf-8")
    # return json.loads(data)
    data = json.loads(response.text)
    
#     print(data);
    
    return data
    
def moving_avg(signal , avg):
    
    avg_len = len(signal) - avg + 1;
        
    avg_sig = np.zeros((avg - 1 ,1))
    
    
    for i in range(avg_len):
        
        start= 0 + i
        
        end = avg - 1 + i;
        
        avg_sig_val = np.mean(signal[start:end]);
        
#         print(avg_sig_val)
        
        avg_sig = np.append(avg_sig , avg_sig_val)
    
        
    return avg_sig


# def pattern_1 ( peaks_valleys):
#     
#     for i in range(len(peaks_valleys) - 5):
#         
#     return 0    
    