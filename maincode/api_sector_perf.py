import requests as req
import numpy as np
import json
from urllib.request import urlopen
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

url_1 = ("https://financialmodelingprep.com/api/v3/historical-sectors-performance?limit=50&apikey=ee74a2831784bf661aeeeefb557a43cd")

def get_jsonparsed_data(url):
    
    response = req.get(url)
    # data = response.read().decode("utf-8")
    # return json.loads(data)
    data = json.loads(response.text)
    return data

finan_perf_df = pd.DataFrame(get_jsonparsed_data(url_1))

finan_perf_df['3_Day_rolling'] =  finan_perf_df['technologyChangesPercentage'].rolling(3, center=True).mean()

# for column in finan_perf_df.columns[1:]:

#     print (finan_perf_df[column].name)
#     plt.plot(finan_perf_df['date'] , finan_perf_df[column])

plt.plot(finan_perf_df['date'] , finan_perf_df['technologyChangesPercentage'])
plt.plot(finan_perf_df['date'] ,finan_perf_df['3_Day_rolling'])
plt.show()