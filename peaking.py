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

from_year = '2016'
to_year = '2017'


url_2 = ("https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?from=" + from_year + "-03-12&to=" + to_year + "-03-12&apikey=ee74a2831784bf661aeeeefb557a43cd")

def get_ratios(url):
    
    response = req.get(url)
    # data = response.read().decode("utf-8")
    # return json.loads(data)
    data = json.loads(response.text)
    
    return data

data_ratio = get_ratios(url_2);

fin_ratio = pd.DataFrame(data_ratio['historical'])

fin_ratio = fin_ratio.iloc[::-1]

print(fin_ratio.iloc[::-1])





