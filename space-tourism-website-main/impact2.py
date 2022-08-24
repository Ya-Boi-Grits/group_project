from cmath import nan
from multiprocessing.sharedctypes import Value
from xml.etree.ElementTree import tostring
from flask_app.models.strategy import Strategy
import requests
import pandas as pd
import mplfinance as mpf
import numpy as np
#import pandas_ta as ta
#import matplotlib.pyplot as plt
#import plotly.graph_objects as pgo
api_key = 'LyK2ZaoUk6E_SFXXqZDFbau87U63LR2v'
ticker = 'BTCUD'
indicator_one = 20
indicator_two = 30


request = requests.get(
    f'https://api.polygon.io/v2/aggs/ticker/X:{ticker}/range/1/day/2022-01-01/2022-06-30?adjusted=true&sort=asc&limit=1000&apiKey={api_key}')
response = request.json()
# Parses through data and organizes it in a pandas dataframe
df = pd.DataFrame(response['results'])
df.columns = ['Volume', 'Weighted Avg', 'Open',
              'Close', 'High', 'Low', 'date', 'Transactions']
# Turns the date column from miliseconds or whatever it is into an actual date
df['date'] = pd.to_datetime(df['date']/1000, unit='s')
# Sets the date column to the itterator instead of standard list index
df.set_index('date', inplace=True)
# this is all closing prices in returned as floats
all_closing_prices = df.loc[:, 'Close']
all_closing_prices_list = all_closing_prices.values.tolist()
# print(all_closing_prices_list)


def find_sma(lst, y):  # sma is needed for first calculation of ema
    x = y - 1
    first = lst[0:x]

    num = 0
    for z in first:
        num += z
    first_sma = num/y
    # print(first_sma)
    return first_sma


f_sma = find_sma(all_closing_prices_list, indicator_one)


def find_multiplier(indicator_one):
    multiplier = 2 / (indicator_one + 1)
    return multiplier


mult = find_multiplier(indicator_one)

# test_muiltiplier = find_multiplier(indicator_one)

# input closes of the price from df, sma from earlier function, mulitplier from earlier function and the indicator_one or second ema setting


def find_ema(lst, sma, multiplier, indicator_one):
    ema_lst = []
    num = 1

    while num < indicator_one:
        ema_lst.append(np.NaN)
        num += 1

    ema_lst.append(sma)

    while num < len(lst):
        ema = lst[num] * multiplier + ema_lst[-1] * (1 - multiplier)
        ema_lst.append(ema)
        num += 1

    return ema_lst


lst_of_ema = find_ema(all_closing_prices_list, f_sma, mult, indicator_one)

df['EMA1'] = lst_of_ema

s_sma = find_sma(all_closing_prices_list, indicator_two)

s_mult = find_multiplier(indicator_two)

second_ema_lst = find_ema(all_closing_prices_list,
                          s_sma, s_mult, indicator_two)

df['EMA2'] = second_ema_lst

df['IS NEG/POS'] = df['EMA1'] - df['EMA2']

df['IS NEG/POS'] = df['IS NEG/POS'].fillna(0)

lst = []
compare = 'neg'
in_trade = False

for time, value in df["IS NEG/POS"].items():
    if value == 0:
        lst.append(np.NaN)
        continue
    else:
        if value > 0 and compare == 'neg' and in_trade == False:
            compare = 'pos'
            in_trade = True
            lst.append("BUY")

        elif value < 0 and compare == 'pos' and in_trade == True:
            compare = 'neg'
            in_trade = False
            lst.append("SELL")

        elif value > 0 and in_trade == True:
            compare = 'pos'
            lst.append(np.NaN)

        elif value < 0 and in_trade == False:
            compare = 'neg'

            lst.append(np.NaN)

df['Buy/Sell'] = lst

buy = 0
profit_loss = 0

for date, value in df['Buy/Sell'].iteritems():
    if value == 'BUY':
        buy = float(df['Close'][date])

    elif value == 'SELL':
        xx = buy - float(df['Close'][date])
        xy = xx/buy

        profit_loss = profit_loss + xy


def plot_ema(df, ticker):
    # Creates a custom ema indicator to plot of graph
    # ema = mpf.make_addplot(df['Close'].ewm(
    #     span=indicator_one, adjust=False).mean(), color='g')
    both_emas = df[['EMA1', 'EMA2']]
    ema_plots = mpf.make_addplot(both_emas)
    # This code actually creates the graph and adds desired indicators. The THICK GREEN line is the ema.
    return mpf.plot(df, type='candle', volume=True, addplot=(ema_plots), title=f'{ticker} - January to June [2022]', ylabel='Price')


plot_ema(df, ticker)
