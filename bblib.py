import requests
import pandas as pd
import pprint
import json
import numpy as np
from mail_lib import send_mail
import math



def build_endpoint(symbol,timeframe,limit):
    base_url = "https://api.binance.com/api/v3/"
    endpoint = f"klines?symbol={symbol}&interval={timeframe}&limit={limit}"
    url = base_url + endpoint
    return url

def get_klines(url):
    candles = requests.get(url).text
    candles = json.loads(candles) # powerful
    return candles

def get_bollinger(candles):
    # keep 5 columns only
    for line in candles:
        del line[5:]

    symbol_df = pd.DataFrame(candles, columns=['date','open','high','low','close'])
    # compute SMA 20
    period = 20
    symbol_df['sma'] = round(symbol_df['close'].rolling(period).mean(),8)
    # std deviation
    symbol_df['std'] = symbol_df['close'].rolling(period).std()
    symbol_df['upper'] = symbol_df['sma']  + (2 * symbol_df['std'])
    symbol_df['lower'] = symbol_df['sma']  - (2 * symbol_df['std'])

    # date column as index in human readable format
    symbol_df.set_index('date',inplace=True)
    symbol_df.index = pd.to_datetime(symbol_df.index,unit='ms')

    # process overbought or oversold flag, convert to float for this purpose
    close_list = pd.to_numeric(symbol_df['close'], downcast='float')
    upper_list = pd.to_numeric(symbol_df['upper'], downcast='float')
    lower_list = pd.to_numeric(symbol_df['lower'], downcast='float')

    symbol_df['buy'] = pd.to_numeric(np.where(close_list < lower_list,   symbol_df['close'], np.NaN ), downcast='float')
    symbol_df['sell'] = pd.to_numeric(np.where(close_list > upper_list,   symbol_df['close'], np.NaN ), downcast='float')

    return symbol_df

def process_bb_overbought_logic(lastline,symbol,timeframe):
    # seek sell signal
    if(math.isnan(lastline.iloc[0]['sell'])):
        """ no sell signal """
        print('do nothing')

    else:
        print(lastline.iloc[0]['sell'])
        print("SHORT")
        send_mail("yvon.huynh@gmail.com",f"shorter {symbol} timeframe {timeframe}",f"shorter  {symbol}")

def process_bb_oversold_logic(lastline,symbol,timeframe):
    # seek buy signal
    if(math.isnan(lastline.iloc[0]['buy'])):
        """ no buy signal """
        print('do nothing')

    else:
        print(lastline.iloc[0]['buy'])
        print("LONG")
        send_mail("yvon.huynh@gmail.com",f"long {symbol}  timeframe {timeframe}",f"Long {symbol}")