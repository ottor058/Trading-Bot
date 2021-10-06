# Use this module to access functions from other files --> Fetch Market data
import datetime as dt
import pandas as pd
from pandas.io.parsers import read_csv
import pandas_datareader as web

# Fetch TICKER data

def fetch_ticker_data(ticker):
    start = dt.datetime(1990,1,1)
    end = dt.datetime(2021,10,24)     
    daily = web.DataReader(ticker, 'yahoo', start, end)
    daily.to_csv(ticker + '.csv')
