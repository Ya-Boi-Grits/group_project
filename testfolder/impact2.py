import requests
import pandas as pd
import mplfinance as mpf
import numpy as np
#import pandas_ta as ta
#import matplotlib.pyplot as plt
#import plotly.graph_objects as pgo
api_key = 'LyK2ZaoUk6E_SFXXqZDFbau87U63LR2v'
# These are the variables the user will be able to alter
crypto_ticker = 'BTCUSD'
limit = '1000'  # this may never be used
passed_ema = 10


request = requests.get(
    f'https://api.polygon.io/v2/aggs/ticker/X:{crypto_ticker}/range/1/day/2022-07-01/2022-07-31?adjusted=true&sort=asc&limit={limit}&apiKey={api_key}')
response = request.json()
# Parses through data and organizes it in a pandas dataframe
df = pd.DataFrame(response['results'])
df.columns = ['Volume', 'Weighted Avg', 'Open',
              'Close', 'High', 'Low', 'date', 'Transactions']
# Turns the date column from miliseconds or whatever it is into an actual date
df['date'] = pd.to_datetime(df['date']/1000, unit='s')
# Sets the date column to the itterator instead of standard list index
df.set_index('date', inplace=True)
print(df)


# def avg_high(df):
#     all_highs = 0
#     for each_high in df['High']:
#         all_highs += each_high
#     average_high = all_highs / 31
#     print(average_high)
#     return average_high


# def avg_low(df):
#     all_lows = 0
#     for each_low in df['Low']:
#         all_lows += each_low
#     average_low = all_lows / 31
#     print(average_low)
#     return average_low


# take_profit = avg_high(df)
# take_loss = avg_low(df)


# def plot_ema(df, passed_ema, crypto_ticker, take_profit, take_loss):
#     # Creates a custom ema indicator to plot of graph
ema = mpf.make_addplot(df['Close'].ewm(
    span=passed_ema, adjust=False).mean(), color='g')
#     print(df)

#     # This code actually creates the graph and adds desired indicators. The THICK GREEN line is the ema.
#     return mpf.plot(df, type='candle', volume=True, title=f'{crypto_ticker} - July 2022',
#                     ylabel='Price', addplot=(ema), mav=4, hlines=dict(hlines=[take_loss, take_profit], colors=['g', 'r'], linestyle='-.'))


# plot_ema(df, passed_ema, crypto_ticker, take_profit, take_loss)
