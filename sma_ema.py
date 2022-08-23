from cmath import nan
import requests
import pandas as pd
# import mplfinance as mpf
import numpy as np
#import pandas_ta as ta
#import matplotlib.pyplot as plt
#import plotly.graph_objects as pgo
api_key = 'LyK2ZaoUk6E_SFXXqZDFbau87U63LR2v'
# These are the variables the user will be able to alter
crypto_ticker = 'BTCUSD'
limit = '1000'  # this may never be used
passed_ema = 20
second_ema = 50


request = requests.get(
    f'https://api.polygon.io/v2/aggs/ticker/X:{crypto_ticker}/range/1/day/2022-04-01/2022-07-31?adjusted=true&sort=asc&limit={limit}&apiKey={api_key}')
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
# this is all closing prices in returned as floats
all_closing_prices = df.loc[:, 'Close']
print(all_closing_prices)

def find_sma(lst, y): # sma is needed for first calculation of ema
    x = y - 1
    first = lst[0:x]

    num = 0
    for z in first:
        num+= z
    first_sma = num/y

    return first_sma




#EMA = Closing price x multiplier + EMA (previous day) x (1-multiplier)

# multiplier = [2 ÷ (period + 1)]

def find_multiplier(period):
    multiplier = 2 / (period +1)
    return multiplier


def find_ema(lst, sma, multiplier, period): # input closes of the price from df, sma from earlier function, mulitplier from earlier function and the passed_ema or second ema setting
    ema_lst = []
    num = 0
    while num < period:
        ema_lst.append(nan)
        num+=1

    ema_lst.append(sma)

    while num < len(lst):
        ema = lst[num] * multiplier + ema_lst[-1] * (1 - multiplier)
        ema_lst.append(ema)
        num+=1

    return ema_lst



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
# ema = [mpf.make_addplot(df['Close'].ewm(
#     span=passed_ema, adjust=False).mean(), color='g'),
#     mpf.make_addplot(df['Close'].ewm(
#     span=second_ema, adjust=False).mean(), color='g')
#     ]
#     print(df)

#     # This code actually creates the graph and adds desired indicators. The THICK GREEN line is the ema.
#     return mpf.plot(df, type='candle', volume=True, title=f'{crypto_ticker} - July 2022',
#                     ylabel='Price', addplot=(ema), mav=4, hlines=dict(hlines=[take_loss, take_profit], colors=['g', 'r'], linestyle='-.'))


# plot_ema(df, passed_ema, crypto_ticker, take_profit, take_loss)
